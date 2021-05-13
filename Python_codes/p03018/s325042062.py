s = input()
new_s = s.replace('BC', 'X')

count = 0
a = 0
for si in list(new_s):
  if si == 'A':
    count += 1
  elif si == 'X':
    a += count
  else:
    count = 0
print(a)