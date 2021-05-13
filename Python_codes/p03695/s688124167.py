n,*l=map(int,open(0).read().split())
s,c=set(),0
for i in l:
  if i<3200: s|={i//400}
  else: c+=1
print(max(1,len(s)),len(s)+c)