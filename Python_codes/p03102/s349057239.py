N,M,C = map(int,input().split())
B = list(map(int,input().split()))
count = 0
value = 0
for i in range(N):
  A = list(map(int,input().split()))
  for j in range(len(A)):
    value = value + A[j] * B[j]
  if value + C > 0:
    count += 1
  value = 0
print(count)