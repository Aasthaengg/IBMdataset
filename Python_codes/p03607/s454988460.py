from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n):
    a = input()
    d[a] += 1
ans = sum([v % 2 for v in d.values()])
print(ans)