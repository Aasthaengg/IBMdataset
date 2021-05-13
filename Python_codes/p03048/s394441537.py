
r,g,b,n=map(int,input().split())
ans=0
r,g,b=sorted([r,g,b])[::-1]
for i in range(n//r+1):
    for j in range(n//g+1):
        k=n-i*r-j*g
        if(k<0):
            break
        if(k>=0 and k%b==0):
            ans+=1
print(ans)