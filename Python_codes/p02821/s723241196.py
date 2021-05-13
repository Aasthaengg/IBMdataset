from bisect import bisect_right

N, M = map(int, input().split())
*A, = map(int, input().split())
INF = 10**12
A.sort()
ac = [0]*(N+1)
for i in range(1, N+1):
    ac[i] = ac[i-1]+A[i-1]

def f(x):
    v = 0
    for i in A:
        v += N-bisect_right(A, x-i)
    return v

def g(l):
    ans = INF
    for i in A:
        res = bisect_right(A, l-i)
        if 0<=res<N:
            ans = min(ans, A[res]+i)
    return ans

l, r = 0, INF+1
while r-l>1:
    m = (l+r)//2
    if f(m)>=M:
        l = m
    else:
        r = m

ans = 0
for i in A:
    v1 = N-bisect_right(A, r-i)
    ans += ac[N]-ac[N-v1]+v1*i
ans += (M-f(r))*g(l)

print(ans)