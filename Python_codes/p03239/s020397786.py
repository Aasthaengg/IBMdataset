n, t = map(int, input().split())
C = []
a = 0
for i in range(n):
    c, time = map(int, input().split())
    if time <= t:
        C.append(c)
    else :
        a += 1
C.sort()
print('TLE' if a == n else C[0])
