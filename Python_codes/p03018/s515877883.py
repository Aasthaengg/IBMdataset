import sys

def f(s):
    if s=="A":
        return 0
    elif s=="B":
        return 1
    else:
        return 2

S=list(map(f,input()))
N=len(S)

if N<=2:
    print(0)
    sys.exit()

T=0
U=0

I=0
K=0
while I<N-2:
    if (S[I]==0) and (S[I+1]==1) and (S[I+2]==2):
        U+=1
        T+=U
        I+=3
    elif S[I]==0:
        U+=1
        I+=1
    elif (S[I]==1) and (S[I+1]==2):
        T+=U
        I+=2
    else:
        U=0
        I+=1

if (S[-2]==1 and S[-1]==2) and S[-3]!=0:
    T+=U
    
print(T)
