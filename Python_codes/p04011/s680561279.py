N = int(input())
K = int(input())
X = int(input())
Y = int(input())
c = 0
for i in range(1,N+1):
  if i <= K:
    c += X
  elif i >= K + 1:
    c += Y
    
print(c)