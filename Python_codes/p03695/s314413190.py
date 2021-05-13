n=int(input())
a=list(map(int,input().split()))
x=[0]*9
for i in a:
    x[min(i//400,8)]+=1
ans=0
for i in range(8):
    if x[i]>0:
        ans+=1
mini=max(1,ans)
maxe=ans+x[8]
print(mini,maxe)

