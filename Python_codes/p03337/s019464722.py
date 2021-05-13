a, b = map(int, input().split())
f = a + b
s = a - b
t = a * b
ans = max(max(f, s), t)
print(ans)