s = input()
k = len(s)
a = s.count('0')
b = s.count('1')
ans = 0
if a >= b:
  ans = k - a + b
else:
  ans = k + a - b
print(ans)