a = list(input())
b = list(input())

c = len(a)

d = 0

for i in range(c):
  if a[i] == b[i]:
    d = d
  else:
    d = d + 1
    
print(d)