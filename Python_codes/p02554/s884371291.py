n = int(input())
ans = 0
num = 1
for i in range(n):
  num *= 10
  num %= 10 ** 9 + 7
ans += num
num = 1
for i in range(n):
  num *= 9
  num %= 10 ** 9 + 7
ans -= num * 2
num = 1
for i in range(n):
  num *= 8
  num %= 10 ** 9 + 7
ans += num
while ans < 0:
  ans += 10 ** 9 + 7
print(ans)