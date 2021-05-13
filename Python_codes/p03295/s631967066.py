n, m = map(int, input().split())

req = []
for i in range(m):
    a, b = map(int, input().split())
    req.append((b-1, a-1))

req.sort()

removed = 0
last = 0
for b, a in req:
    if a >= last:
        removed += 1
        last = b

print(removed)