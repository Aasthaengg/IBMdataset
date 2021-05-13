import itertools
l=['M','A','R','C','H']
c = itertools.combinations(l, 3)
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
ans=0
for i in c:
  ans+=MARCH[i[0]]*MARCH[i[1]]*MARCH[i[2]]
print(ans)