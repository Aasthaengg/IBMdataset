from itertools import combinations
n = int(input())
x = n if n % 2 else n+1
ans = []
for v, v2 in combinations(range(1, n+1), 2):
    if v+v2 == x:
        continue
    ans.append((v, v2))
print(len(ans))
for edge in ans:
    print(*edge)
