N = int(input())

l = 0
j = 0
r = N -1

print(0, flush=True)
a = input()
if a == 'Vacant':
  exit()
b = a
while r - l > 1:
  i = (r + l)//2
  print(i, flush=True)
  a = input()
  if a == 'Vacant':
    exit()
  if abs(i-j)%2 == 0:
    if a == b:
      if i > j:
        l = i
      else:
        r = i
    else:
      if i > j:
        r = i
      else:
        l = i
  else:
    if a == b:
      if i > j:
        r = i
      else:
        l = i
    else:
      if i > j:
        l = i
      else:
        r = i
      
  b = a
  j = i

print(l, flush=True)
a = input()
if a == 'Vacant':
  exit()
  
print(r, flush=True)
