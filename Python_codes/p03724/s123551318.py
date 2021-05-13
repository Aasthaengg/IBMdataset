n, m = [int(w) for w in input().split()]

node = [0] * (n+1)

for i in range(m):
    a, b = [int(w) for w in input().split()]
    node[a] ^= 1
    node[b] ^= 1

cond = all([w == 0 for w in node])
print("YES" if cond else "NO")
