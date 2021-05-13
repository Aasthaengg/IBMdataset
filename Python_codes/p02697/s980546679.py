n,m= map(int, input().split())
ans=[]
if n%2==1:
    for i in range(m):
        ans.append(i+1)
        ans.append(n-1-i)

else:
    if m<=n//4:
        for i in range(m):
            ans.append(n//2+1+i)
            ans.append(n//2-i)

    else:
        for i in range(m-n//4):
            ans.append(2+i)
            ans.append(n-i)
        for i in range(n//4):
            ans.append(n//2+1+i)
            ans.append(n//2-i)


print(*ans)