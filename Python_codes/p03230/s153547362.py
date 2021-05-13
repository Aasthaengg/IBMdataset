N = int(input())
if N == 1:
  print('Yes')
  print(2)
  print(1, 1)
  print(1, 1)
  quit()

S = [{1, 2}, {1, 3}, {2, 3}]
n = 3
while n < N:
  l = len(S)
  s = set()
  for i in range(l):
    n += 1
    S[i].add(n)
    s.add(n)
  S.append(s)

if n == N:
  print('Yes')
  print(len(S))
  for s in S:
    print(len(s), *s)
else:
  print('No')