o = 0
N,R = map(int, input().split())

n = N
r = R

if n <= 10:
    o = R + 100 * (10-N)
else:
    o =R

print(o)