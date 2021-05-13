import math
N, K = map(int, input().split())

def return_prob(x):
  if K <= x:
    return 1
  else:
    return 1 / (2 ** math.ceil(math.log2(K/x)))

prob = 0
for i in range(1, N+1):
  prob += return_prob(i)
prob /= N
print(prob)