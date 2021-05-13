N, L = map(int, input().split())

if L-1 >= 0:
  i = 1
elif L-1 >= -N:
  i = -(L-1)
else:
  i = N

A = (N-1)*(L-1) + sum([n for n in range(1, N+1)]) - i
print(A)