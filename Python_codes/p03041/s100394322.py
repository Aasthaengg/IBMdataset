n,k = map(int,input().split())
s = input()
kb = ''
if k >= 2:
  kb = s[:k-1]
kk = s[k-1]
ka = ''
if k < len(s):
  ka = s[k:]

if kk == 'A':
  print(kb + 'a' + ka)
  exit()
if kk == 'B':
  print(kb + 'b' + ka)
  exit()
if kk == 'C':
  print(kb + 'c' + ka)
  exit()  