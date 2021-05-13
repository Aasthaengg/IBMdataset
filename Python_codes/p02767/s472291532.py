N = int(input())
A = list(map(int, input().split()))
S = sum(A)
x = round(S/N)
ans = 0
for i in range(N):
  ans += (A[i] - x)**2
print(ans)

