N = int(input())
ans = 0
if N % 2 == 1:
  print(0)
  exit()
while N:
  N //= 5
  ans += N // 2
print(ans)