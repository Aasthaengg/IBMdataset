s=input()
q=int(input())
h=0
m=''
u=''
for _  in range(q):
  d=input()
  if '2' in d:
    a,b,c=map(str,d.split())
    if b=='1':
      if h%2==0:
        m+=c
      else:
        u+=c
        
    else:
      if h%2==0:
        u+=c
      else:
        m+=c
        
  else:
    h+=1
    
M=list(m)
G=list(reversed(M))
GG=''.join(G)
s=GG+s+u
if h%2==0:
  print(s)
else:
  f=list(s)
  g=list(reversed(f))
  print(''.join(g))