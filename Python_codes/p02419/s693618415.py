W=input().upper()
r=0
while 1:
  w=input()
  if w == 'END_OF_TEXT':break
  r+=len([x for x in w.upper().split() if x == W])
print(r)