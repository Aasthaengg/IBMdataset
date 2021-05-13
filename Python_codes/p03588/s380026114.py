N = int(input())
maxi = 0
ans = 0
for i in range(N):
  A, B = map(int, input().split())
  if maxi < A:
    maxi = A
    ans = A + B
print(ans)
