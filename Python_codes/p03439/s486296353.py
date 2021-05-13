
def chk(n,S):
    if S[n]=="":
        print(n,flush=True)
        temp=input()
        if temp=="Vacant":
            exit()
        else:
            S[n]=temp
            return S[n]
    else:return S[n]

def chk2(S1,S2):
    T1=chk(S1,S)
    T2=chk(S2,S)
    if (S2-S1)%2!=0:
        if T1==T2:
            return True
        else:
            return False
    elif (S2-S1)%2==0:
        if T1!=T2:
            return True
        else:
            return False

def chk3(S1,S2):
    chk(S1,S)
    chk(S2,S)
    Sm=(S1+S2)//2
    if chk2(S1,Sm):
        chk3(S1,Sm)
    else:
        chk3(Sm,S2)

N=int(input())

S=[""]*N

chk3(0,N-1)

