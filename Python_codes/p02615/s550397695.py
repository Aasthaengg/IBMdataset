N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0

if N % 2 == 1:
  ans += A[0]
  ans += A[N//2]
  for i in range(1,N//2):
    ans += A[i]*2
else:
  ans += A[0]
  for i in range(1,N//2):
    ans += A[i]*2
print(ans)