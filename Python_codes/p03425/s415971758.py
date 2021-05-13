MARCH = {'M':0,'A':0,'R':0,'C':0,'H':0}
N=int(input())
for i in range(N):
  s=str(input())
  if s[0]=='M':
    MARCH['M']+=1
  elif s[0]=='A':
    MARCH['A']+=1
  elif s[0]=='R':
    MARCH['R']+=1
  elif s[0]=='C':
    MARCH['C']+=1
  elif s[0]=='H':
    MARCH['H']+=1
ans = MARCH['M']*MARCH['A']*MARCH['R']\
  +MARCH['M']*MARCH['A']*MARCH['C']\
  +MARCH['M']*MARCH['A']*MARCH['H']\
  +MARCH['M']*MARCH['R']*MARCH['C']\
  +MARCH['M']*MARCH['R']*MARCH['H']\
  +MARCH['M']*MARCH['C']*MARCH['H']\
  +MARCH['A']*MARCH['R']*MARCH['C']\
  +MARCH['A']*MARCH['R']*MARCH['H']\
  +MARCH['A']*MARCH['C']*MARCH['H']\
  +MARCH['R']*MARCH['C']*MARCH['H']
print(ans)