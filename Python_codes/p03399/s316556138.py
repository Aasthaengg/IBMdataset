a = []
for i in range(4):
  a.append(0)
  a[i] = int(input())
print(min(a[0],a[1])+min(a[2], a[3]))