import sys
input()
ac,wa={*()},{}
nc=np=0
for ln in sys.stdin:
    p,S=ln.split()
    if p in ac:
        continue
    if p not in wa:
        wa[p]=0
    if S=='AC':
        ac.add(p)
        nc+=1
        np+=wa[p]
    else:
        wa[p]+=1

print(nc,np)
