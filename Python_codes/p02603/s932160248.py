N = int(input())
A = list(map(int, input().split()))
A.append(0)

buy = A[0]
ans = 1000
for i in range(1, N):
  if A[i] > A[i+1] and buy < A[i]:
    ans = ans % buy + ans // buy * A[i]
    buy = 500
  elif buy > A[i]:
    buy = A[i]
print(ans)