n,k = map(int, input().split())
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)
def comb(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res
cm = comb(n-1,2)

if n==2 and k>=1:
    print(-1)
    exit()

if cm < k:
    print(-1)
    exit()

ans=[]
for i in range(1,n):
    ans.append([1,i+1])

from itertools import *
cnt=0
for e in combinations(range(2,n+1),2):
    if cnt== cm-k:
        break
    cnt+=1
    ans.append([e[0],e[1]])

print(len(ans))
for a in ans:
    print(*a)