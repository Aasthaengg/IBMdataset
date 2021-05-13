N = int(input())
A = list(map(int, input().split()))
A.sort(reverse = True)
ans = A[0]

if N%2 == 0:
  for i in range(1,int(N/2)):
    ans = ans + A[i]*2
if N%2 == 1:
  for i in range(1,int((N-1)/2)):
    ans = ans + A[i]*2
  ans += A[int((N-1)/2)]
print(ans)

