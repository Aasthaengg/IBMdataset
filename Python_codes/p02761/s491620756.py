nm=input("").split(" ")
n=int(nm[0])
m=int(nm[1])
lists=[-1]*n
ss=0
if(n==1):
    tt=-1
    for i in range(m):
        sc=input("").split(" ")
        s=int(sc[0])
        c=int(sc[1])
        if(tt==-1):
            tt=c
        elif(tt==c):
            None
        else:
            ss=1
    if(ss==1):
        print(-1)
    elif(m==0):
        print(0)
    else:
        print(tt)
        

else:
    for i in range(m):
        sc=input("").split(" ")
        s=int(sc[0])
        c=int(sc[1])
        if(s==1 and c==0):
            ss=1
        elif(lists[s-1]==-1):
            lists[s-1]=c
        elif(lists[s-1]==c):
            None
        else:
            ss=1
    if(ss==1):
        
            
        print(-1)
        
    else:

        pp=""
        for i in range(n):
            if(lists[i]==-1 and i!=0):
                pp+="0"
            elif(lists[i]==-1):
                pp+="1"
            else:
                pp+=str(lists[i])
        print(int(pp))
            
