a = list('abcdefghijklmnopqrstuvwxyz')
n = int(input()) - 1

ans = ""
while True:
  b = n // 26
  c = n % 26
  if b == 0:
    ans = a[c] + ans
    break
  elif b == 1:
    ans = a[b - 1] + a[c] + ans
    break
  else:
    ans = a[c] + ans
    n = b - 1
    
print(ans)