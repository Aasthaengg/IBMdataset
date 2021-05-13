a, b, c, d = map(int, input().split())

x = [a, b]
y = [c, d]
if a <= 0 <= b:
    x.append(0)
if c <= 0 <= d:
    y.append(0)

ans = -10 ** 19
for p in x:
    for q in y:
        ans = max(ans, p * q)

print(ans)