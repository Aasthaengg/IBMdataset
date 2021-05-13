from collections import defaultdict
n, m = map(int, input().split())
a = list(map(int, input().split()))
b, c = [0] * m, [0] * m
data = defaultdict(int)
for i in range(m):
    b[i], c[i] = map(int, input().split())
    data[c[i]] += b[i]

for x in a:
    data[x] += 1
data = sorted(data.items(), key = lambda x: x[0])
i = len(data) - 1
cnt = 0
ans = 0
while 1:
    x = min(n - cnt, data[i][1])
    ans += x * data[i][0]
    i -= 1
    cnt += x
    if cnt == n:
        break
print(ans)
