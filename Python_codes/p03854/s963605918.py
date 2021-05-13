a,b,c,d=[i[::-1] for i in ['dream','dreamer','erase','eraser']]
s,j=input()[::-1],True
while j:
  j=False
  for i in [a,b,c,d]:
    if s.startswith(i): s=s[len(i):];j=True
print('YNEOS'[len(s)>0::2])