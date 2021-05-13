import sys
s = int(input())
a = []
for i in range(1,1000001):
  if i ==1:
    a.append(s)
  else:
    if a[i-2]%2 ==0:
      x = a[i-2]/2
      if x in a:
        print(i)
        sys.exit()
      a.append(x)
    else:
      x = 3 * a[i-2] + 1
      if x in a:
        print(i)
        sys.exit()
      a.append(x)