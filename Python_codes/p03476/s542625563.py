p = [2, 3]
for i in range(5, 10 ** 5 + 1, 2):
  flag = True
  j = 0
  while p[j] * p[j] <= i:
    if i % p[j] == 0:
      flag = False
      break
    j += 1
  if flag:
    p.append(i)

tf = [False] * (10 ** 5 + 1)
for i in p:
  tf[i] = True

like = [0]
for i in range(1, 10 ** 5 + 1):
  if tf[i] and tf[(i + 1) // 2]:
    like.append(like[-1] + 1)
  else:
    like.append(like[-1])

ans = []
q = int(input())
for _ in range(q):
  i, j = map(int, input().split())
  i -= 1
  ans.append(like[j] - like[i])

for i in ans:
  print(i)