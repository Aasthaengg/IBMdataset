N = int(input())
V = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
m = 0
for i in range(N):
  if (V[i]-C[i]) > 0:
    m = m + V[i]-C[i]
print(m)