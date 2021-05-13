n = int(input().split()[0])

if n < 1200:
  ans = 'ABC'
elif n < 2800:
  ans = 'ARC'
else:
  ans = 'AGC'
  
print(ans)
