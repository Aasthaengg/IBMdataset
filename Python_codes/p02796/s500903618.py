n = int(input())
data = []
for i in range(n):
    x, l = map(int, input().split())
    data.append([x, l])
data = sorted(data, key = lambda x: x[0] + x[1])
ans = 0
pre = -(10 ** 10)
for i in range(n):
    if data[i][0] - data[i][1] >= pre:
        ans += 1
        pre = data[i][0] + data[i][1]

print(ans)