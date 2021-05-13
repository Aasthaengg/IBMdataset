N , T = map(int, input().split())
l_c = []

for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        l_c.append(c)

for j in range(len(l_c)):
    if l_c[j] == min(l_c):
        print(l_c[j])
        exit()

print('TLE')