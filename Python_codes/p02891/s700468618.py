S=input()
K=int(input())
h=1
b=0
l=[]
f=False
c1=0
c2=0
c3=0
c4=0
r=[]
v=[]
vf=False
vf1=False
vf2=False
for i in range(len(S)-1):
    if S[i]==S[i+1]:
        if i==0:
            c1=1
            c3=1
        if (i+1)==(len(S)-1):
            c2=1
            c4=1
        h+=1
        f=True
    else:
        f=False
    if not f:
        if h!=1:
            l.append(h)
            if c3==1:
                r.append(h)
                c3=0
            if c4==1:
                r.append(h)
                c4=0
        h=1
#print(l)
if f:
    l.append(h)
    #print(l)
    if c4==1:
        r.append(h)
        c4=0
#print(l)
if S[0]==S[-1]:
    #print(l)
    if c1==1 and c2==1:
        if len(l)==1:
            s=len(S)*K
            print(s//2)
            exit()
        else:
            v.append(l[0])
            v.append(l[-1])
            l[-1]+=l[0]
            del l[0]
            vf=True
    elif c1==1:
        #l[0]+=1
        v.append(l[0])
        #v.append(l[-1])
        l[0]+=1
        v.append(l[0])
        del l[0]
        vf1=True
    elif c2==1:
        #l[-1]+=1
        #v.append(l[0])
        v.append(l[-1])
        l[-1]+=1
        v.append(l[-1])
        del l[-1]
        vf2=True
    else:
        if len(S)==1:
            print(K//2)
            exit()
        print(K-1)
        exit()
h=0
if vf:
    h+=v[0]//2
    h+=v[-1]//2
    for i in range(len(l)):
        if i==(len(l)-1):
            h+=(l[i]//2)*(K-1)
        else:
            h+=(l[i]//2)*K
elif vf1:
    h+=(v[1]//2)*(K-1)
    h+=(v[0]//2)
    for i in range(len(l)):
        h+=(l[i]//2)*K
elif vf2:
    h+=(v[1]//2)*(K-1)
    h+=(v[0]//2)
    for i in range(len(l)):
        h+=(l[i]//2)*K
else:
    for i in range(len(l)):
        h+=(l[i]//2)*K

#print(l)
print(h)