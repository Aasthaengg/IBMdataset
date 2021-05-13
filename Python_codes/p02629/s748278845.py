n = int(input())
res = ''

while n > 0:
  if n % 26 != 0:
    res = chr(ord('a') + (n % 26) - 1) + res
    n = n // 26
  else:
    res = 'z' + res
    n = (n // 26) - 1
print(res)