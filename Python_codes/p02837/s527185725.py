n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
  num = int(input())
  for j in range(num):
    person, state = map(int, input().split())
    a[i].append([person-1, state])
honest = 0
for i in range(1, 2**n):
  flag = True
  for j in range(n):
    if (i>>j)&1 == 1:
      for x, y in a[j]:
        if (i>>x)&1 != y:
          flag = False
          break
  if flag:
    honest = max(honest, bin(i)[2:].count('1'))
print(honest)