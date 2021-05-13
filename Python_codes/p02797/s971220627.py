n,k,s = map(int,input().split())
if s < 10 ** 9:
    z = ((str(s) + ' ') * k) + ((str(s+1) + ' ') * (n-k))
else:
    z = ((str(s) + ' ') * k) + (('1' + ' ') * (n-k))
print(z)