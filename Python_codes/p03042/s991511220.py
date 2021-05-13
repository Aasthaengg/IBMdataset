s=list(input())
if s[0]=='0':
  t=int(s[1])
  
else:
  t=int(''.join(s[:2]))
if s[2]=='0':
  u=int(s[3])
else:
  u=int(''.join(s[2:]))

if t>=1 and t<=12:
  if u>=1 and u<=12:
    print('AMBIGUOUS')
    
  else:
    print('MMYY')
    
else:
  if u>=1 and u<=12:
    print('YYMM')
    
  else:
    print('NA')