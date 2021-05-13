h, w = list(map(int, input().split()))
power = [list(map(int, input().split())) for i in range(10)]

for i in range(10):
    for j in range(10):
        for k in range(10):
            power[j][k] = min(power[j][i] + power[i][k], power[j][k])

ans = 0
for i in range(h):
    wall = list(map(int, input().split()))
    for item in wall:
        if item < 0:  continue
        ans += power[item][1]
print(ans)