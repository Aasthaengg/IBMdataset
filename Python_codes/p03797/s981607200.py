n,m = map(int,input().split())
r = min(n, m//2)
m -= r*2
if m <= 3:
    pass
else:
    r += m//4


print(r)