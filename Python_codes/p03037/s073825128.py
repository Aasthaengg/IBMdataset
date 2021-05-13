N, M = map(int, input().split())
x = [0] * (N + 1)

for i in range(M):
  l, r = map(int, input().split())
  x[l - 1] += 1
  x[r] -= 1
  
for i in range(1, N + 1):
  x[i] += x[i - 1]
  
#print(x)
print(x.count(M))