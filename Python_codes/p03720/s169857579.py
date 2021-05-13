N,M = [int(i) for i in input().split()]
list = []

for i in range(M):
  a,b = [int(i) for i in input().split()]
  list.append(a)
  list.append(b)

for i in range(1,N+1):
  print(list.count(i))
