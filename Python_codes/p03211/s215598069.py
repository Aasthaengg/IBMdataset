a = input()
b = abs(753 - int(a[:3]))
for i in range(1, len(a)-2):
  c = abs(753 - int(a[i:i+3]))
  if b >= c :
    b = c
print(b)