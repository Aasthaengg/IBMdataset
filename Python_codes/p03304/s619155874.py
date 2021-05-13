n,m,d = map(int,input().split())
if d >=1:
    prb = ((2*d)/n)*(1/n)+((n-2*d)/n)*(2/n)
else:
    prb = 1/n

print(prb*(m-1))
