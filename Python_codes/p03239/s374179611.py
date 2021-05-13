N, T = map(int, input().split())

x = None
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        x = c if x is None or x > c else x

if x is None:
    print('TLE')
else:
    print(x)