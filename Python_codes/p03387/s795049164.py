a = sorted(list(map(int, input().split())))

s = sum(a)
if s%2==a[2]%2:
  if a[2]%2==a[1]%2:
    print((a[2]-a[1])//2+(a[2]-a[0])//2)
  else:
    a[1] += 1
    a[0] += 1
    print((a[2]-a[1])//2+(a[2]-a[0])//2+1)
else:
  a[2] += 1
  a[1] += 1
  if a[2]%2==a[1]%2:
    print((a[2]-a[1])//2+(a[2]-a[0])//2+1)
  else:
    a[1] += 1
    a[0] += 1
    print((a[2]-a[1])//2+(a[2]-a[0])//2+2)