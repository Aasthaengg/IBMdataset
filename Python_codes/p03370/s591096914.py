n, x = map(int, input().split())
m = []
ans = n
for i in range(n):
  m.append(int(input()))
x -= sum(m)
ans += x // min(m)
print(ans)