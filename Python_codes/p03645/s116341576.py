n, m = input().split()

p = set()
q = set()
for _ in range(int(m)):
    a, b = input().split()
    if a == "1":
        p.add(b)
    elif b == n:
        q.add(a)
else:
    if p & q:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")