N = int(input())
B = list(map(int,input().split()))
A = 0
for i in range(N-1):
  if i == 0:
    A += B[0]
  else:
    A += min(B[i],B[i-1])
A += B[N-2]
print(A)