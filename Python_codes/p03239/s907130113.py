n, T = map(int, input().split())
min = 2000
for i in range(n):
    c, t = map(int, input().split())
    if t <= T and min > c:
        min = c
print(min if min != 2000 else "TLE")
