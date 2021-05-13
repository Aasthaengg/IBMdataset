A,B,C,D=map(int,input().split())
i=0
while A>0 and C>0:
    C=C-B
    i+=1
    if A>0 and C>0:
        A=A-D
        i+=1
    else:
        break
if i%2!=0:
    print('Yes')
if i%2==0:
    print('No')