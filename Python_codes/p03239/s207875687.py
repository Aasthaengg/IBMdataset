N, T = map(int, input().split())

min_c = 1000
b = False

for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        min_c = min(c, min_c)
        b = True

print(min_c if b else 'TLE')
