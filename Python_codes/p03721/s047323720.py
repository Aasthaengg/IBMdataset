from collections import defaultdict

n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

nums, numd = set(), defaultdict(int)
for a, b in ab:
    nums.add(a)
    numd[a] += b
for i in sorted(nums):
    k -= numd[i]
    if k <= 0:
        print(i)
        break
