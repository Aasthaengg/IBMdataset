n,m,d=map(int,input().split())

if d==0:
    p=1/n
else:
    p=2*(n-d)/n**2

print((m-1)*p)