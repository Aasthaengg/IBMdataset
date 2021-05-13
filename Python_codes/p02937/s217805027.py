import sys
s=input()
ss=s+s
t=input()
l=len(s)
d={}
for i in range(26):
    d[chr(ord("a")+i)]=i
ref=[[] for _ in range(26)]
for i in range(2*l):
    ref[d[ss[i]]].append(i)

for i in range(26):
    if ref[i]==[]: ref[i].append(-1)

tmp=[0 for i in range(26)]
next=[[-1]*26 for i in range(l)]
for i in range(l):
    tmp[d[s[i]]]+=1
    for j in range(26):
        next[i][j]=ref[j][tmp[j]]

p=s.find(t[0])
if p==-1: print(-1);sys.exit()
ans=p

for i in range(1,len(t)):
    x=d[t[i]]
    q=next[p][x]
    if q==-1: print(-1);sys.exit()
    ans+=-p+q
    p=q%l
print(ans+1)