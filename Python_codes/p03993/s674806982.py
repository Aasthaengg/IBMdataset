N = int(input())
A =  list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
  j = A[i-1]
  if j > i and A[j-1] == i:
    ans += 1
print(ans)