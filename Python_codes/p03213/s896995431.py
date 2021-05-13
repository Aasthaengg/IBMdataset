from collections import defaultdict

def dfs(i, comb):
    key = (i, comb)
    if key in memo:
        return memo[key]
    if comb == 75:
        return 1
    if i == m:
        return 0
    k, v = p[i]
    res = 0
    for j in range(v + 1):
        if comb * (j + 1) <= 75:
            res += dfs(i + 1, comb * (j + 1))
    memo[key] = res
    return res

n = int(input())
index = defaultdict(int)

for x in range(2, n + 1):
    y = 2
    while y ** 2 <= x:
        while x % y == 0:
            x //= y
            index[y] += 1
        y += 1
    if x > 1:
        index[x] += 1

*p, = index.items()
m = len(p)
memo = {}
print(dfs(0, 1))
