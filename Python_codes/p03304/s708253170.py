n,m,d=map(int,input().split())

if d==0:
    aaa=aaa=n*(m-1)/(n**2)
else:
    aaa=(n-d+(n-(d+1)+1))*(m-1)/(n**2)

print(aaa)
