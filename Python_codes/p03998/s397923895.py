Sa=input()
Sb=input()
Sc=input()
a,b,c=0,0,0
d='a'
for i in range(len(Sa)+len(Sb)+len(Sc)+3):
  if d=='a':
    if a==len(Sa):
      print('A')
      exit()
    d=Sa[a]
    a+=1
  elif d=='b':
    if b==len(Sb):
      print('B')
      exit()
    d=Sb[b]
    b+=1
  elif d=='c':
    if c==len(Sc):
      print('C')
      exit()
    d=Sc[c]
    c+=1