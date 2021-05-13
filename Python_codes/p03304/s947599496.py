n,m,d=map(int,input().split())
v=1/n if d==0 else 2*(n-d)/n/n
v*=(m-1)
print(v)