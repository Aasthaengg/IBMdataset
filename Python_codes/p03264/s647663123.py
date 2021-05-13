K = int(input())
Q = 0
A = 0
for i in range(1,K+1):
  if i % 2 == 0:
    Q += 1
  else:
    A += 1
print(Q*A)