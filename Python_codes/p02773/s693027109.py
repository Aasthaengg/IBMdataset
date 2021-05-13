import collections
n = int(input())
s = [input() for _ in range(n)]

c = collections.Counter(s)
max_cnt = max(c.values())

ans = [k for k, v in c.items() if v == max_cnt]
ans.sort()
for i in ans:
    print(i)