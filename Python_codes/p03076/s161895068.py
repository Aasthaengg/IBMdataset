A = sorted( [int(input()) for i in range(5)], key = lambda x : - x % 10)

ans = 0
for i in range(4):
  ans += A[i]
  if ans % 10 > 0:
    ans += 10 - ans % 10
print(ans + A[4])