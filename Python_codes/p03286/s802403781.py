n = int(input())
ans = ''
while n != 0:
    if n % (-2) == 0:
        n //= (-2)
        ans +='0'
    else:
        n = (n - 1) // (-2)
        ans +='1'
if ans=='':
  print(0)
else:
  print(ans[::-1])