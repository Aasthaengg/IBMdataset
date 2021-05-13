s = int(input())
a = [s]
count = 1

for i in range(100000):
  if a[i] % 2 == 0:
    b = a[i]/2
  else:
    b = 3*a[i]  + 1  
  a.append(b)
  count += 1
  if a.count(b) >1:
    break

print(count)