n,m,d=map(int,input().split())
print(2*(m-1)*(n-d)/n**2 if d else (m-1)/n)