N = int(input())
i = 1
ans = 0
while N:
  ans += i
  N //= 2
  i *= 2
print(ans)