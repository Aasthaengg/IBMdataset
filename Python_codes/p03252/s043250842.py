S=input()
T=input()
s=dict()
for i in range(len(S)):
    a=S[i]
    if a in s:
        s[a]+=1
    else:
        s[a]=1

t=dict()
for i in range(len(T)):
    a=T[i]
    if a in t:
        t[a]+=1
    else:
        t[a]=1

l=[]
r=[]
for idx in s:
    a=s[idx]
    l.append(a)
for idx in t:
    a=t[idx]
    r.append(a)

l.sort()
r.sort()
if len(l)!=len(r):
    print("No")
    exit()
for i in range(len(l)):
    if l[i]==r[i]:
        pass
    else:
        print("No")
        exit()

print("Yes")