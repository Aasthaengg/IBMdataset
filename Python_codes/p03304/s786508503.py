n,m,d=map(int,input().split())

p=2*(n-d)/(n**2) if d!=0 else n/(n**2)
print(p*(m-1))