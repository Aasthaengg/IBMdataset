n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7
plus = []
minus=[]
for i in A:
    if i>=0:
        plus.append(i)
    else:
        minus.append(i)
ok = False
if len(plus)>0:
    if n==k:
        ok = (len(minus)%2==0)
    else:
        ok = True
else:
    ok = (k%2==0)
ans = 1
if not ok:
    A.sort(key=abs)
    for i in range(k):
        ans *= A[i]
        ans %= mod
else:
    plus.sort()
    minus.sort(reverse=True)
    if k%2 == 1:
        ans *= plus.pop()
    P = []
    while len(plus) >= 2:
        P.append((plus.pop())*(plus.pop()))
    while len(minus) >= 2:
        P.append((minus.pop())*(minus.pop()))
    P.sort(reverse=True)
    for i in range(k//2):
        ans *= P[i]
        ans %= mod
print(ans)
