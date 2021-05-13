N, T = map(int, input().split())
c = [0] * N
t = [0] * N
for i in range(N):
    c[i], t[i] = map(int, input().split())

z = zip(c, t)
z = sorted(z)
c, t = zip(*z)

for i in range(N):
    if t[i] <= T:
        print(c[i])
        exit()
print('TLE')
