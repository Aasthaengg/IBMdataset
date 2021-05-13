N = int(input())
A = list(map(int, input().split()))
ans = 'APPROVED'

for i in range(len(A)):
  if A[i] % 2 == 0:
    if A[i] % 3 == 0 or A[i] % 5 == 0:
      continue
    else:
      ans = 'DENIED'

print(ans)