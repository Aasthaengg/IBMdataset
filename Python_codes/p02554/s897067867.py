n = int(input())
a,b,c = 1,1,1
for i in range(n):
  a *= 10
  b *= 9
  c *= 8
  a %= 10** 9 + 7
  b %= 10** 9 + 7
  c %= 10** 9 + 7
print((a - 2 * b +c)%(10** 9 + 7))