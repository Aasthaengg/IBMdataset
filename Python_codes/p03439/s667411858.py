N=int(input())
l,r=0,N
now=-1
print(0)
a=input()
li=['Male','Famale']
if(a=='Vacant'):
    print(0)
    exit()
elif(a=='Male'):
    now=0
else:
    now=1
for _ in range(19):
    Q=((l+r)//2)%N
    print(Q)
    ans=input()
    if(ans=='Vacant'):
        print(Q%N)
        exit()
    res=-1
    if(ans=='Male'):
        res=0
    else:
        res=1
    if((Q-l-1)%2==1 and res!=now) or ((Q-l-1)%2==0 and res==now):
        r=Q
    else:
        l=Q
        now=res
print((l+r)//2%N)