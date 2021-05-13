from itertools import zip_longest

n, m = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(m)]

A.sort()
BC.sort(key=lambda x: -x[1])

stack = []
i = 0
while len(stack) < n and i < m:
  for _ in range(BC[i][0]):
    stack.append(BC[i][1])
    if len(stack) >= n:
      break
  i += 1

ans = 0
for a, s in zip_longest(A, stack, fillvalue=0):
  ans += max(a, s)

print(ans)