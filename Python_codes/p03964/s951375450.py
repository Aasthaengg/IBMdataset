n = int(input())
nt, na = 1, 1
for _ in range(n):
  t, a = map(int, input().split())
  x, y = -(-nt//t), -(-na//a)
  m = max(x, y)
  nt, na = t*m, a*m
print(nt+na)
