n,m,d=map(int,input().split())
num=2 if d>0 else 1
print(num*(n-d)*(m-1)/n**2)