s = input()
def WA():
  print('WA')
  exit()
if s[0] != 'A':
  WA()
if ord(s[-1]) < ord('a') or ord('z') < ord(s[-1]):
  WA()
if ord(s[1]) < ord('a') or ord('z') < ord(s[1]):
  WA()
s = s[1:]
ccnt = 0
for i in s[1:-1]:
  if i == 'C':
    ccnt += 1
  elif ord(i) < ord('a') or ord('z') < ord(i):
    print('WA')
    exit()
if ccnt != 1:
  print('WA')
  exit()
else:
  print('AC')