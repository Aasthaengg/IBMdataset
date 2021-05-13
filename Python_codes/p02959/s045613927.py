N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = [0]*(N+1)
for i in range(N+1):
  ans[i] = A[i]
for i in range(N):
  rem = ans[i]-B[i]
  ans[i] = max(rem,0)
  if (rem<0):
    ans[i+1] = max(ans[i+1]+rem,0)
print(sum(A)-sum(ans))