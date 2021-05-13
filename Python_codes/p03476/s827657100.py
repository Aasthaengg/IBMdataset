S = set()
L = [True]*(10**5+1)
L[0] = False
L[1] = False
for i in range(2, 10**5+1):
    if L[i]:
        S.add(i)
        for j in range(i*2, 10**5+1, i):
            L[j] = False


def prime(n):
    return n in S


M = [0]*(5*10**4+1)
for i in range(1, 5*10**4+1):
    m = 2*i-1
    n = i
    M[i] = M[i-1]+(prime(m) & prime(n))

Q = int(input())
ans = [0]*Q
for _ in range(Q):
    l, r = list(map(int, input().split()))
    i = (l+1)//2
    j = (r+1)//2
    ans[_] = M[j]-M[i-1]
for _ in range(Q):
    print(ans[_])