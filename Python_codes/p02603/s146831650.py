N = int(input())
A = list(map(int,input().split()))

minval = 0
ans = 1000

for i in range(1, N):
  if A[i] > A[minval]:
    pstock = ans // A[minval]
    ans = ans%A[minval] + A[i]*pstock
  minval = i

print(ans)