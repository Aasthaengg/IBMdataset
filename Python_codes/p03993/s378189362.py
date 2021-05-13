N = int(input())
A = [-1] + list(map(int,input().split()))
ans = 0
for i in range(1,N+1):
  if A[A[i]] == i and i<A[i]: ans += 1
print(ans)