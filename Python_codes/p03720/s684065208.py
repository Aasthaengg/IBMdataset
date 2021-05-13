N, M = input().split(' ')
N = int(N)
M = int(M)
citys = []
for i in range(M):
  a, b = input().split(' ')
  a = int(a)
  b = int(b)
  citys.append(a)
  citys.append(b)
for i in range(1, N+1):
  print(citys.count(i))