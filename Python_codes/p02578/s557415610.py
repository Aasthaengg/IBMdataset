N = int(input())
A = list(map(int, input().split()))
total = 0
Amax = A[0]
for i in range(1,len(A)):
  if Amax > A[i]:
    total += Amax-A[i]
  else:
    Amax = A[i]
print(total)