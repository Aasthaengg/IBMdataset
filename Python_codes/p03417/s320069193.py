n,m=map(int,input().split())
print(n*m-2*(n+m)+4 if n!=1 and m!=1 else max(n*m-2,1))