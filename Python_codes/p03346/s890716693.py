import sys
input=sys.stdin.readline
n=int(input())
l=[int(input()) for i in range(n)]
li=[0 for i in range(n+1)]
for i,j in enumerate(l):
    li[j]=i
ans=n-1
i=1
ms=1
while i<n:
    if li[i]<li[i+1]:
        ms+=1
        i+=1
    else:
        ans=min(ans,n-ms)
        ms=1
        i+=1
print(min(ans,n-ms))