n = int(input())

edges = []
 
for i in range(1, n + 1):
  for j in range(i + 1, n + 1):
    if n % 2 == 1 and i + j != n \
    or n % 2 == 0 and i + j != n + 1:
      edges.append((i, j))

print(len(edges))

for i, j in edges:
	print(i, j)