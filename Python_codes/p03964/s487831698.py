n = int(input())
L = []
for i in range(n):
	L.append([int(i) for i in input().split()])

x = L[0][0]
y = L[0][1]

for i in range(n-1):
  n = max(-(-x//L[i+1][0]), -(-y//L[i+1][1]))
  x = n*L[i+1][0]
  y = n*L[i+1][1]

print(x+y)