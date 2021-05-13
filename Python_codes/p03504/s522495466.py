import numpy as np
n,C = map(int,input().split())
ch = [[] for _ in range(30)]
for _ in range(n):
    s,t,c = map(int,input().split())
    if s>t:
        s,t = t,s
    ch[c-1].append((s,t))

lst = []
for i in range(30):
    if len(ch[i])!=0:    
        for i, (ns,nt) in enumerate(ch[i]):
            if i==0:
                s,t = ns, nt
            else:
                if ns == t:
                    t = nt
                else:
                    lst.append((s,t))
                    s,t = ns, nt
        else:
            lst.append((s,t))
    
d = [0]*(10**6)
for s,t in lst:
    d[s-1] += 1
    d[t] -= 1
d = np.cumsum(d)
print(min(max(d), C))