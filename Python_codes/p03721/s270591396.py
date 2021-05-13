from collections import Counter
n, k = map(int, input().split())
d = Counter([])
for i in range(n):
    a, b = map(int, input().split())
    d[a] += b
ans = 1
cnt = 0
while cnt < k:
    cnt += d[ans]
    ans += 1

print(ans - 1)