n, m = [int(w) for w in input().split()]

ed = [0] * n
for i in range(m):
    a, b = [int(w) - 1 for w in input().split()]
    ed[a] += 1
    ed[b] += 1
print("\n".join([str(w) for w in ed]))
