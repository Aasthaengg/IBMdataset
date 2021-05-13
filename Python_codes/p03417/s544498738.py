n,m=map(int,input().split())

if n>=3 and m>=3:
    ans=n*m-(2*n+2*m-4)
elif n==2 or m==2:
    ans=0
elif n==1 and m==1:
    ans=1
else:
    ans=n*m-2

print(ans)