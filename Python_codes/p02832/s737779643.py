n=int(input())
a=list(map(int,input().split()))
k=1;ans=0
c=[]
for i in range(n):
    ans=0
    if a[i]==k:
       ans+=i
       c.append(ans)
       k+=1
if len(c)==0:
    print(-1)
else:
    print(n-len(c))