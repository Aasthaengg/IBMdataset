n,m,d=map(int,input().split())

k=n if d==0 else 2*(n-d)
ans=(k/n**2)*(m-1)

print(ans)