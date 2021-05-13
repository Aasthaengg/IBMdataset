n=int(input())
if n==1:
    print(1)
    exit()
from itertools import accumulate
a=[0]*(4500)
for i in range(1,4500):
    a[i-1]=i

ac=list(accumulate(a))

for i in range(n+1):
    if ac[i]+a[i+1]>=n:
        maxi=a[i+1]
        break

a=[i for i in range(1,maxi)]

ans=[maxi]
n-=maxi

def solve(n):
    if n==1:
        ans.append(1)
        return 0
    a=[0]*4500
    for i in range(1,4500):
        a[i-1]=i
    
    ac=list(accumulate(a))
    
    for i in range(n+1):
        if ac[i]+a[i+1]>=n:
            maxi=a[i+1]
            break
    ans.append(maxi)
    n-=maxi
    return n

while n>0:
    n=solve(n)

for i in ans:
    print(i)