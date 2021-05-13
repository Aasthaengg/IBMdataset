N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [input().split() for l in range(N)]

i = 0
for a in A:
  s = 0
  for x, y in zip(a, B):
    s += int(x) * y

  if s + C > 0:
    i += 1
  else:
    pass


print(i)