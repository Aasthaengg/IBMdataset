n = input()
aa = map(int, input().split())
bb = map(int, input().split())

d = 0
for a, b in zip(aa, bb):
    if a >= b:
        d += a - b
    else:
        d -= (b - a) // 2

print("Yes" if d <= 0 else "No")