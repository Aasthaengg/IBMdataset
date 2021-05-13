N = int(input())
A = list(map(int, input().split()))
ans = 30
for i in range(N):
  count = 0
  while A[i] % 2 == 0:
    A[i] //= 2
    count += 1
  if count < ans:
    ans = count
print(ans)