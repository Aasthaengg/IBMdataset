n,m,d = (int(i) for i in input().split())
if d: print(2*(m-1)*(n-d)/(n**2))
else: print((m-1)/n)