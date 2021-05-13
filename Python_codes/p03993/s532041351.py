from collections import defaultdict

n = int(input())
alst = list(map(int, input().split()))
dd = defaultdict(int)

for i, num in enumerate(alst, start = 1):
    s = str(min(i, num)) + "-" + str(max(i, num))
    dd[s] += 1

ans = 0
for i, j in dd.items():
    if j == 2:
        ans += 1
print(ans)