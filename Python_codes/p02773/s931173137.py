from collections import defaultdict

n = int(input())
l = defaultdict(int)
m = 0
for _ in range(n):
    s = input()
    l[s] += 1
    m = max(m, l[s])

ans = []
for k, v in l.items():
    if v == m:
        ans.append(k)
ans.sort()
for s in ans:
    print(s)
