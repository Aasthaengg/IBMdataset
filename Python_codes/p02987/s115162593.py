s = input()

cnt = []
for i in range(4):
  cnt.append(s.count(s[i]))
  
if all(n == 2 for n in cnt):
  print('Yes')
else:
  print('No')