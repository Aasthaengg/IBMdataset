import sys
s = input()

l1 = ['L', 'U', 'D']
l2 = ['R', 'U', 'D']

cnt = 0
for i in range(len(s)):
  if i == 0 or i%2 == 0:
    if s[i] not in l2:
      print('No')
      sys.exit()
  else:
    if s[i] not in l1:
      print('No')
      sys.exit()

print('Yes')