n = int(input())
P = [int(input()) for _ in range(n)]
Q = [0]*(n+1)
for i, j in enumerate(P):
  Q[j-1] = i+1
count = 0
m = 0
for i in range(n):
  count += 1
  if Q[i] > Q[i+1]:
    m = max(m, count)
    count = 0
print(n-m)