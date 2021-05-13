n = int(input())
a = list(map(int, input().split()))
s = min(a)
b = max(a)
si = a.index(s)
bi = a.index(b)
op = []
if s + b >= 0:
    for i in range(n):
        if a[i] < 0:
            op.append((bi+1, i+1))
    for i in range(n-1):
        op.append((i+1, i+2))
else:
    for i in range(n):
        if a[i] > 0:
            op.append((si+1, i+1))
    for i in reversed(range(n-1)):
        op.append((i+2, i+1))
print(len(op))
for x, y in op:
    print(x, y)