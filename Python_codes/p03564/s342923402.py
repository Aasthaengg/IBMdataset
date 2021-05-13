mini = 1025
N = int(input())
K = int(input())
for i in range(N+1):
  x = 1
  xx = 2**i
  xxx = K*(N-i) +xx
  
  if xxx < mini:
    mini = xxx
print(mini)