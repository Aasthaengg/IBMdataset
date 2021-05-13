A = list(map(int, input().split()))
A = sorted(A)

if (A[2]-A[0]-(A[2]-A[1]))%2==0:
  ans = A[2]-A[1]+(A[2]-A[0]-(A[2]-A[1]))//2
else:
  ans = A[2]-A[1]+(A[2]-A[0]-(A[2]-A[1]))//2+2
                   
print(ans)