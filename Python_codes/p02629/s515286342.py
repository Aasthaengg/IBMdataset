n = int(input())

ans = ""
for _ in range(1, 15):
  x = n % 26
  if x == 0:
    x = 26
  ans += chr(96 + x)
  n -= x
  if n == 0:
    break
  n //= 26
  
print(ans[::-1])