N=int(input())
d={}
for _ in range(N):
    s=input()
    d[s]=d.get(s,0)+1

tmp=sorted(d.items(), key=lambda x: (x[0])) 
l=sorted(tmp, key=lambda x: x[1], reverse=True) 
c=l[0][1]

for s,v in l:
  if v==c: print(s)
  else: break