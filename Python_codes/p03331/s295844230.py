n = int(input())

def digit(n):
  digit = 0
  while n > 0:
    digit += n % 10
    n //= 10
  return digit
    
  

ans = 1000000
for i in range(1,n):
  if ans > digit(i) + digit(n-i):
    ans = digit(i) + digit(n-i)
print(ans)