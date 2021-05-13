s=input()
p=input()
sl = [i for i in s]
pl = [i for i in p]
lenp=len(p)
pp=pl[-1]
el=[i for i,x in enumerate(sl) if x==pp]
check=0
for i in el:
    pcheck=-1
    while True:
        if sl[i]==pl[pcheck]:
            i-=1
            pcheck-=1
        else:
            break
        if pcheck+lenp<=0:
            check+=1
            break
    if check==1:
        break
if check==0:
    print("No")
else:
    print("Yes")

