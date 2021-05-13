from itertools import accumulate
S=list(map(len,input().split("T")))
x,y=map(int,input().split())
x=abs(x-S[0])
y=abs(y)
L=S[2::2]
R=S[1::2]
La=list(accumulate(L))
Ra=list(accumulate(R))
sumL=sum(L)
sumR=sum(R)
flag=0
if sumL>=x and sumR>=y and (sumL-x)%2==0 and (sumR-y)%2==0 and flag==0:
    setL1={0}
    setR1={0}
    gL=(sumL-x)//2
    gR=(sumR-y)//2
    if gL==0:
        flag=1
    else:
        for cnt,i in enumerate(L):
            setL=setL1
            setL1=set()
            s=setL1.add
            h=sumL-La[cnt]
            for j in setL:
                k=i+j
                #if k<gL and h+k>=gL:
                s(k)
                #if j<gL and h+j>=gL:
                s(j)
                if k==gL:
                    flag=1
                    break
            if flag==1:
                break
    if flag==1:
        if gR==0:
            flag=2
        else:
            for cnt,i in enumerate(R):
                setR=setR1
                setR1=set()
                s=setR1.add
                h=sumR-Ra[cnt]
                for j in setR:
                    k=i+j
                    #if k<gR and h+k>=gR:
                    s(k)
                    #if j<gR and h+j>=gR:
                    s(j)
                    if k==gR:
                        flag=2
                        break
                if flag==2:
                    break
if flag==2:
    print("Yes")
else:
    print("No")