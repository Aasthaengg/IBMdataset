d={}
for _ in range(int(input())):
 s=input()
 d[s]=d.get(s,0)+1
c=max(d.values())
for s,v in sorted(d.items()):
 if v==c: print(s)