from collections import defaultdict


N, *A = map(int, open(0).read().split())
ans = defaultdict(int)
for a in A:
    ans[a] += 1
print(sum(v % 2 for v in ans.values()))
