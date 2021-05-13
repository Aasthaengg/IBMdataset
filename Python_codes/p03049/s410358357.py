n,*s=open(0).read().split()
w=''
b=[]
a=[]
e=""
for i in s:
    if i[-1]=='A' and i[0]=="B":
        w+=i
    elif i[-1]=='A':
        a.append(i)
    elif i[0]=='B':
        b.append(i)
    else:
        e+=i
#print(w)
a=iter(a)
b=iter(b)
if len(w)!=0:
    w=next(a,'')+w+next(b,'')
i,j=next(a,''),next(b,'')
while i!='' or j!='':
    w+=i+j
    i,j=next(a,''),next(b,'')
w+=e
print(w.count('AB'))