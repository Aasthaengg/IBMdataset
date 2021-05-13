N,M = map(int,input().split())
*A, = map(int,input().split())

A.sort(reverse=True)

def count(i,B):
    B = B - A[i]
    l = -1
    r = N
    while l+1<r:
        j = (l+r)//2
        if A[j] >= B:
            l = j
        else:
            r = j
    return r

l = 0
r = 10**5*3
while l+1<r:
    i = (l+r)//2
    S = 0
    for j in range(N):
        S += count(j,i)
    if S==M:
        r = i
        break
    elif S>M:
        l = i
    else:
        r = i

ans = 0
tmp = 0
SA = [0]*(N+1)
for j in range(N):
    SA[j+1] = SA[j] + A[j]
for j in range(N):
    c = count(j,r)
    ans += A[j]*c + SA[c]
    tmp += c
if M>tmp:
    n = 0
    for j in range(N):
        c = count(j,r)
        if c==N: continue
        n = max(n,A[j] + A[c])
    ans += n*(M-tmp)
print(ans)