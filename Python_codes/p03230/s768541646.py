n = int(input())
tri = [1]
for i in  range(2, 450):
    tri.append(i * (i + 1) // 2)
if not n in tri:
    exit(print("No"))
print("Yes")
ind = tri.index(n) + 2
ans = [[] for i in range(ind)]
cur = 1
print(ind)
for i in range(ind):
    for j in range(i + 1, ind):
        ans[i].append(cur)
        ans[j].append(cur)
        cur += 1
for i in ans:
    print(len(i), *i)