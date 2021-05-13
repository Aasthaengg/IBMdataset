N=int(input())

T=[0]*9

S=list(map(int,input().split()))

for i in range(N):
    if S[i]<400:
        T[0]=1
    elif S[i]<800:
        T[1]=1
    elif S[i]<1200:
        T[2]=1
    elif S[i]<1600:
        T[3]=1
    elif S[i]<2000:
        T[4]=1
    elif S[i]<2400:
        T[5]=1
    elif S[i]<2800:
        T[6]=1
    elif S[i]<3200:
        T[7]=1
    else:
        T[8]+=1

goukeimin=0



for i in range(8):
    goukeimin+=T[i]
if goukeimin==0:
    print(1,sum(T))
else:
    print(goukeimin,sum(T))
        
        
