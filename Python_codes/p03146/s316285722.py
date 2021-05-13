s = int(input())
a = [s]
for i in range(1000000):
  if a[i]%2==0:
    b=a[i]/2
  else:
    b=a[i]*3+1
  if b in a:
    print(i+2)
    break
  else:
    a.append(b)