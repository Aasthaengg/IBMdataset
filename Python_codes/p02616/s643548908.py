n,k=map(int, input().split())
a = list(map(int, input().split()))
mod=10**9+7
if n==k:
    ans=1
    for i in range(k):
        ans*=a[i]
        ans%=mod
    print(ans)
    exit()
minus=[i for i in a if i<0]
plus=[i for i in a if i>=0]
from collections import deque
minus=deque(sorted(minus))
plus=deque(sorted(plus,reverse=True))

n_minus=len(minus)
n_plus=len(plus)
if n_minus==n:
    ans=1
    if k%2==0:
        for i in range(k):
            ans*=minus.popleft()
            ans+=mod
            ans%=mod
        print(ans)
        exit()
    else:
        for i in range(k):
            ans*=minus.pop()
            ans+=mod
            ans%=mod
        print(ans)
        exit()

ans=1
while k>1:
    if n_minus>1 and n_plus>1 and k!=3:
        if minus[0]*minus[1]>=plus[0]*plus[1]:
            n_minus-=2
            k-=2
            for _ in range(2):
                ans*=minus.popleft()
                ans%=mod
        else:
            n_plus-=2
            k-=2
            for _ in range(2):
                ans*=plus.popleft()
                ans%=mod
    elif n_minus>1 and n_plus>2 and k==3:
        ans*=max(minus[0]*minus[1]*plus[0],plus[0]*plus[1]*plus[2])
        ans%=mod
        k-=3
    elif n_minus>1:
        n_minus-=2
        k-=2
        for _ in range(2):
            ans*=minus.popleft()
            ans%=mod
    elif n_plus>1:
        n_plus-=2
        k-=2
        for _ in range(2):
            ans*=plus.popleft()
            ans%=mod

if k==1:
    if plus:
        ans*=plus.popleft()
        ans%=mod

print(ans)
