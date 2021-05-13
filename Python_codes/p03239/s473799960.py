n,T = map(int,input().split())
c = 500000
for i in range(n):
    a,b = map(int,input().split())
    if T >= b:
        c = min(c,a)
print(c if c < 500000 else 'TLE')
