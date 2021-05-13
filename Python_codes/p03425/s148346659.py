from itertools import combinations
n = int(input())
arr = [input() for _ in range(n)]

li = ["M", "A", "R", "C", "H"]

result = []
for s in li:
    result.append(len(set([x for x in arr if x[0] == s])))

ans = 0

for x, y, z in combinations(result, 3):
    ans += x * y * z

print(ans)