A = list(map(int, input().split()))
A.sort()
ans = A[2]-A[1]
if (A[2]-(A[2]-A[1]+A[0]))%2==1:
  ans = ans + 2 + (A[2]-(ans+A[0]))//2
else:
  ans = ans + (A[2]-(ans+A[0]))//2
print(ans)