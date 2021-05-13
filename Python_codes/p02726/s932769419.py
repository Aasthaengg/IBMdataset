n,x,y=map(int,input().split())
k=[0]
k*=(n-1)
z=x-y
for i in range(1,n+1):
    for j in range(i+1,n+1):
        ans1=j-i
        ans2=abs(x-i)+abs(y-j)+1
        ans3=abs(x-j)+abs(y-i)+1
        ans=min(ans1,ans2,ans3)
        k[ans-1]+=1
        
for i in range(n-1):
    print(k[i])