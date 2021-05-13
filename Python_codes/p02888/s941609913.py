n=int(input())
l=list(map(int,input().split()))
l.sort()
num=[0]*(max(l)+2)
for i in range(n):
    num[l[i]]=i
for i in range(1,len(num)):
    if num[i]==0:
        num[i]=num[i-1]
ans=0
num3=l[n-1]
for i in range(n-2):
    for j in range(i+1,n-1):
        ans+=max(0,num[min(num3,l[i]+l[j]-1)]-j)
print(ans)
