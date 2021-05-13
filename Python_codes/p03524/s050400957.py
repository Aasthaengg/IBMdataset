S=input()
x=dict()
if len(S)==1:
    print("YES")
    exit()

for i in range(len(S)):
    s=S[i]
    if s in x:
        x[s]+=1
    else:
        x[s]=1
l=[]
cnt=0
for idx in x:
    l.append(x[idx])
    cnt+=1
if len(S)==2 and cnt!=1:
    print("YES")
    exit()

if cnt!=3:
    print("NO")
    exit()
l.sort()
x=l[0]
y=l[1]
z=l[2]
y=y-x
z=z-x
if y>1 or z>1:
    print("NO")
else:
    print("YES")