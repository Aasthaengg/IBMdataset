N = int(input())
A = [int(x) for x in input().split()]
plus = [x for x in A if x > 0]
minus = [x for x in A if x <= 0]
plus.sort()
minus.sort()
minA = minus.pop() if minus else plus.pop(0)
M = sum(plus) - sum(minus)
M += -minA if plus else minA
print(M)
xy = minA
for i in range(N - 1):
  if len(plus) > 1:
    y = plus.pop()
    print('{} {}'.format(xy, y))
    xy -= y
  elif len(plus) == 1:
    x = plus.pop()
    print('{} {}'.format(x, xy))
    xy = x - xy
  else:
    y = minus.pop()
    print('{} {}'.format(xy, y))
    xy -= y