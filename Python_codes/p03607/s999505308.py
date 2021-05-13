from collections import defaultdict
n = int(input())
dd = defaultdict(int)

for i in range(n):
    dd[int(input())] += 1

ans = 0
for k, v in dd.items():
    if v % 2 == 1:
        ans += 1

print(ans)
