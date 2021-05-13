a =[]
b = 0
s = input()
for i in s:
  a.append(i)
  b += 1
print(str(a[0])+str((b-2))+str(a[b-1]))