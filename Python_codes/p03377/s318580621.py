a, b, x = map(int, input().split())
n = 'YES'
if a > x:
  n = 'NO'
elif a+b < x:
  n = 'NO'
print(n)