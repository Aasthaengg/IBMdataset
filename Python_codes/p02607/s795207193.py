N = int(input())
A = [int(i) for i in input().split()]
c = 0

for i in range(N):
  if (i+1) % 2 == 1 and A[i] % 2 == 1:
    c += 1
else:
  print(c)
