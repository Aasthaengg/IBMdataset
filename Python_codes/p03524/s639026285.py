s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')

ans = ''
if a == b == c:
  ans = 'YES'
elif a == b == c - 1:
  ans = 'YES'
elif a == b - 1 == c:
  ans = 'YES'
elif a - 1 == b == c:
  ans = 'YES'
elif a == b == c + 1:
  ans = 'YES'
elif a == b + 1 == c:
  ans = 'YES'
elif a + 1 == b == c:
  ans = 'YES'
else:
  ans = 'NO'
print(ans)