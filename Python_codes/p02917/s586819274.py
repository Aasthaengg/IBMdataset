N = int(input())
if N == 2:
  ans = 2 * int(input())
else:
  B = list(map(int, input().split()))
  ans = B[0] + B[N-2]
  for i in range(1, N-1):
    ans += min(B[i], B[i-1])
print(ans)