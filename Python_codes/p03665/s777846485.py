import math

N,P = map(int,input().split())
A = list(map(int,input().split()))
pascal_triangle = []

memo = [[0 for _ in range(51)] for _ in range(51)]

def c(n,k):
  if memo[n][k] != 0:
      return memo[n][k]
  if(k<=0 or n<=k):
      memo[n][k] = 1
      return 1
  else:
      ans = c(n-1, k-1) + c(n-1, k)
      memo[n][k] = ans
      return ans

for i in range(51):
  pascal_triangle.append([c(i,j) for j in range(i+1)])

Numbers_1 = 0
for i in range(N):
    Numbers_1 += A[i] % 2

Select_0_count = sum(pascal_triangle[N - Numbers_1])

ans = 0

for i in range(Numbers_1+1):
    if i % 2 == P:
        ans += pascal_triangle[Numbers_1][i] * Select_0_count

print(ans)