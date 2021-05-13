x = int(input())
quotient = x // 11
x -= quotient * 11
ans = quotient * 2
if x == 0:
  print(ans)
elif x <= 6:
  print(ans+1)
elif x <= 11:
  print(ans+2)