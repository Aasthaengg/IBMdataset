r,g,b,n=map(int,input().split())
ans=0
for i in range(n//r+1):
    if r*i==n:
        ans+=1
        break
    else:
        for j in range((n-r*i)//g+1):
            if r*i+g*j==n:
                ans+=1
                continue
            else:
                if n-(r*i+g*j)>0 and (n-(r*i+g*j))%b==0:
                    ans+=1

print(ans)