n, t = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]

ct.sort(key=lambda x: x[1])
ct.sort(key=lambda x: x[0])
for i in range(n):
    if ct[i][1] <= t:
        print(ct[i][0])
        exit()
print('TLE')
