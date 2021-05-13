n, m = map(int, input().split())
s = set()
g = set()
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        g.add(b)
    if b == n:
        s.add(a)
x = s & g
if x:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")