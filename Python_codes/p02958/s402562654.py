n,*p=map(int,open(0).read().split());l=len(p)
np=sorted(p);cou=0
for i in range(l):
  if p[i]!=np[i]:cou+=1
print("YES" if (cou==2 or cou == 0) else "NO")