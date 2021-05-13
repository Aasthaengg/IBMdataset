N,Q=map(int,input().split())
S=input()
L=[]
R=[]
C=[0]*N
c=0
for i in range(Q):
    A=list(map(int,input().split()))
    L.append(A[0])
    R.append(A[1])
for i in range(N-1):
    if S[i]=="A" and S[i+1]=="C":
        c+=1
        C[i]=c
    else:
        C[i]=c
C[N-1]=c
S+="X"
for i in range(Q):
    p=0
    if S[R[i]-1]=="A" and S[R[i]]=="C":
        p=C[R[i]-1]-C[L[i]-1]-1
    else:
        p=C[R[i]-1]-C[L[i]-1]
    if S[L[i]-1]=="A" and S[L[i]]=="C":
        p+=1
    print(p)