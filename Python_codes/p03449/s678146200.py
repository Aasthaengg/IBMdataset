import sys
n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
ans=0
if n==1:
    print(a1[0]+a2[0])
    sys.exit()
for i in range(n-1):
    tmp=a2[n-1]
    for j in range(i+1):
        tmp+=a1[j]
    for k in range(i,n-1):
        tmp+=a2[k]
    if tmp>ans:
        ans=tmp
print(ans)