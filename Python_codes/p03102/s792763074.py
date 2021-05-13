n, m, c = [int(x) for x in input().split()]
bb = [int(x) for x in input().split()]
a = [list(map(int, input().split())) for _ in range(n)]

result = 0
for ae in a:
  tmp = sum([a*b for a, b in zip(ae, bb)]) + c
  if tmp > 0:
    result += 1

print(result)