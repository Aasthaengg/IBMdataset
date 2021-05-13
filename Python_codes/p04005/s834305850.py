a = list(map(int, input().split()))
a.sort()

ans = 0
x = 0

for num in a:
  if num%2 == 0:
    print(0)
    x += 1
    break
  
if x == 0:
  ans = a[0] * a[1]
  print(ans)
