N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(N):
  add = 1
  for j in A[:i]:
    if j % 2 == 0: add *= 2
  if A[i] % 2 == 1: add *= 2
  add *= 3 ** (N - i - 1)
  ans += add
print(ans)  