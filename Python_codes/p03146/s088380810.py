import sys

s = int(input())
a = [0, s]
i = 2

while a[-2] != 2 and a[-1] != 1:
  if (a[i-1])%2 == 0:
    a.append(int(a[i-1]/2))
  elif (a[i-1])%2 == 1:
    a.append(int(1+3*a[i-1]))
  i += 1
a.append(4)
a.append(2)
a.append(1)

stuck = []
for i in range(1, len(a)):
  if (a[i]) in stuck:
    print(i)
    sys.exit()
  else:
    stuck.append(a[i])  