from itertools import combinations

n = int(input())
S = [input() for _ in range(n)]

memo = {}
for i in 'MARCH':
    memo[i] = 0

for i in S:
    if i[0] in 'MARCH':
        memo[i[0]] += 1

ans = 0
for i, j, k in combinations('MARCH', 3):
    ans += memo[i] * memo[j] * memo[k]
print(ans)