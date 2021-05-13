import sys
s=input()
t=input()
l=len(s)
d={}
for i in range(26):
    d[chr(ord("a")+i)]=i
ref=[[] for _ in range(26)]
for i in range(l):
    ref[d[s[i]]].append(i)

for i in range(26):
    if ref[i]==[]: ref[i].append(-1)

tmp=[0 for i in range(26)]
next=[[-1]*26 for i in range(l)]
for i in range(l):
    x=d[s[i]]
    tmp[x]=(tmp[x]+1)%len(ref[x])
    for j in range(26):
        next[i][j]=ref[j][tmp[j]]

p=s.find(t[0])
ans=p

if p==-1: print(-1);sys.exit()
for i in range(1,len(t)):
    x=d[t[i]]
    q=next[p][x]
    if q==-1: print(-1);sys.exit()
    ans+=-p+q
    if p>=q: ans+=l
    p=q
print(ans+1)