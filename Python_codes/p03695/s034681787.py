N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(8)]
a = 0
for i in range(N):
  if A[i] < 400:
    B[0] = 1
  elif A[i] < 800:
    B[1] = 1
  elif A[i] < 1200:
    B[2] = 1
  elif A[i] < 1600:
    B[3] = 1
  elif A[i] < 2000:
    B[4] = 1
  elif A[i] < 2400:
    B[5] = 1
  elif A[i] < 2800:
    B[6] = 1
  elif A[i] < 3200:
    B[7] = 1
  else:
    a += 1
b = sum(B)
m = b
M = b + a
if b == 0:
  m = 1
print(m, M, sep=' ')