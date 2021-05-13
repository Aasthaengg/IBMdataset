N = int(input())
A = list(map(int,input().split()))

right = 1
xor = A[0]
sum = A[0]
ans = 0
for left in range(N):
  while right < N and xor ^ A[right] == sum + A[right]:
    xor ^= A[right]
    sum += A[right]
    right += 1
  ans += right - left
  if left == right:
    right += 1
  xor ^=A[left]
  sum -=A[left]
print(ans)