from collections import Counter
n = int(input())
a_ls = list(map(int, input().split()))

c = Counter(a_ls)
edges_ls = [0] * 2
for value, count in c.items():
    if count >= 2:
        edges_ls.append(value)
    if count >= 4:
        edges_ls.append(value)
edges_ls.sort()
ans = edges_ls[-1] * edges_ls[-2]
print(ans)