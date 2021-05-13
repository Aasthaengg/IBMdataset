M, K = list(map(int, input().split()))

if K == 0:
  print("0 0",end = "")
  for i in range(1, pow(2, M)):
    print("", i, i, end = "")
  print()
  exit()

if K == 1 and M == 1:
  print(-1)
  exit()

N = pow(2, M)
if K >= N:
  print(-1)
  exit()
 
if K == 1:
  k = 1
  a = 2
  b = 3
elif K % 2 == 1:
  k = K
  a = 1
  b = K - 1
else:
  k = K
  a = 1
  b = K + 1

print(a, k, end = " ")
for i in range(N):
  if i != a and i != b and i != k:
    print(i, end = " ")
print(a, b, end = " ")
for i in range(N - 1, -1, -1):
  if i != a and i != b and i != k:
    print(i, end = " ")
print(k, b)
