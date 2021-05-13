N = int(input())
K = int(input())
x = 1
  
for i in range(N):
  if x < K:
    x = x*2
  else:
    x = x + K

print(x)