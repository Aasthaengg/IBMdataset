n, m = [int(i) for i in input().split()]
islands = [set() for i in range(n)]
for i in range(m):
    a, b = [int(i) for i in input().split()]
    islands[a-1].add(b)
    islands[b-1].add(a)
f = False
for i in islands[n-1]:
    if 1 in islands[i-1]: f = True
print("POSSIBLE" if f else "IMPOSSIBLE")