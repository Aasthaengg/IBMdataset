a, b = map(int, input().split())
f = a + b
s = a - b
t = a * b
ans = max(f, s, t)
print(ans)