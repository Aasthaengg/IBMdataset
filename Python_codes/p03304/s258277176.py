n,m,d=map(int,input().split())
print((m-1)/n if d==0else 2*(m-1)*(n-d)/n**2)