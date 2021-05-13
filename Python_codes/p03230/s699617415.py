from itertools import combinations
n = int(input())
root = 1 + 8 * n
if int(root ** 0.5) ** 2 != root:
    print('No')
    exit()

k = (1 + int(root ** 0.5)) // 2
ans = [[] for _ in range(k)]

for i, a in enumerate(combinations(range(k), 2)):
    s, t = a
    ans[s].append(i + 1)
    ans[t].append(i + 1)
print('Yes')
print(k)
for List in ans:
    print(k - 1, *List)