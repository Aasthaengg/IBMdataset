
n,m,d = map(int,input().split())

if d != 0:
    x = 2
else:
    x = 1
print (x*(n-d)*(m-1)/(n**2))
