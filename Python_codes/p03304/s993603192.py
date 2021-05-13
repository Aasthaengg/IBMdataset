n,m,d=map(int,input().split())
k=2 if d!=0 else 1
print(k*(m-1)*(n-d)/n**2)