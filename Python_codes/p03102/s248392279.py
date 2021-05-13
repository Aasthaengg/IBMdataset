n, m, c = map(int, input().split())
lb = list(map(int, input().split()))
t = 0

for _ in range(n):
  la = list( map(int, input().split()) )
  s = c
  for i in range(m):
    s += la[i] * lb[i]
  if s > 0:
    t += 1

print(t)