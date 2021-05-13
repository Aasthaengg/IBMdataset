n, m = map(int, input().split())

p = set()
q = set()

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        p.add(b)
    elif b == n:
        q.add(a)
else:
    if p & q:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")