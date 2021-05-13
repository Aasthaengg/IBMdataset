r,g,b,n=map(int,input().split())
ans=0
for i in range(3001):
    for j in range(3001):
        if (r*i+g*j)<=n:
            z=n-(r*i+g*j)
            if z%b==0:
                #print(i,j)
                ans+=1
        
print(ans)

