

N=int(input())

l=0
r=N

print(l,flush=True)
bstate=input()

if bstate!="Vacant":
    while True:
        #c=int((l+r)/2)
        L=int((r-l)/2)
        if (L%2)==0:
            L-=1
        c=l+L
        c=max(l+1,c)
        c=min(r-1,c)
        #print(c,l,r)
        print(c,flush=True)
        state=input()
        if state=="Vacant":
            break

        if state!=bstate:
            l=c
        else:
            r=c

        bstate=state
