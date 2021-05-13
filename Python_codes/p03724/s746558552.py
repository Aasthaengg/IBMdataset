n,m = map(int, input().split())
d = {}
for i in range(m):
    for j in map(int, input().split()):
        d[j] = d.get(j, 0) + 1

if any(i%2 for i in d.values()):
    print("NO")
else:
    print("YES")
