s = input()

wa = False

if s[0] != 'A':
  wa = True
if s[2:-1].count('C') != 1:
  wa = True

l_s = list(s)
  
if 'A' in l_s:
	del l_s[l_s.index('A')]

if 'C' in l_s:
	del l_s[l_s.index('C')]

for c in l_s:
  if c != c.lower():
    wa = True
    
if wa == True:
  print('WA')
else:
  print('AC')