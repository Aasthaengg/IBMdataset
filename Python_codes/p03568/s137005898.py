N = int(input())
A = list(map(int, input().split()))
ans = pow(3,N)
even = 0
for i in range(N):
  if A[i]%2==0:
    even += 1
ans -= pow(2,even)
print(ans)