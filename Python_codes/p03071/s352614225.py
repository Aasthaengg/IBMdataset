a, b = map(int, input().split())

n = 2
total = 0
while n > 0:
  if a > b:
    total=total+a
    a-=1
  else:
    total=total+b
    b-=1
  n-=1
print(total)