n, T = [int(i) for i in input().split()]
mn = 10000
for i in range(n):
    c,t = [int(i) for i in input().split()]
    if t <= T:
        mn = min(mn, c)
print("TLE" if mn == 10000 else mn)
