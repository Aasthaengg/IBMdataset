import sys
s = int(input())

a = [s]

ans = 1
while(True):
  ans += 1
  if a[-1]%2 == 0:
    num = a[-1]//2
  else:
    num = a[-1]*3+1
  for i in range(len(a)):
    if a[i] ==num:
      print(ans)
      sys.exit()

  a.append(num)
