T=[]
for i in range(5):
    T.append(int(input()))
t=[]
for i in range(5):
    t.append(T[i]%10)
a=0
if 0 not in t:
    for i in range(5):
        if t[i]==min(t):
            a=T[i]
            T.remove(T[i])
            break
    for i in range(4):
        a+=((T[i]//10)+1)*10

if 0 in t:
    U=[s for s in T if s%10==0]
    G=[s for s in T if s%10!=0]
    g=[]
    for i in range(len(G)):
        g.append(G[i]%10)
        
    for i in range(len(U)):
        a+=U[i]
        
    for i in range(len(G)):
        if g[i]==min(g):
            a+=G[i]
            G.remove(G[i])
            break
            
    for i in range(len(G)):
        a+=((G[i]//10)+1)*10

print(a)