n,m = (int(x) for x in input().split())

table = [[0] for i in range(n)]
vector = [0 for j in range(m)]

# input table
i = 0
while i < n:
  table[i] = list(int(x) for x in input().split())
  i += 1

# input vector
i = 0
while i < m:
  vector[i] = int(input())
  i += 1

# calc C
for i in table:
  sum = 0
  for idx,j in enumerate(i):
    sum += j * vector[idx]
  print (sum)
