n,m,d = map(int,input().split())
print((n-d)*(m-1)*2/n**2 if d else (n-d)*(m-1)/n**2)