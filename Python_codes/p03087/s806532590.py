N,Q=map(int,input().split())
S=input()
L=[]
R=[]
for i in range(Q):
    LR=list(map(int,input().split()))
    L.append(LR[0]-1)
    R.append(LR[1]-1)

cnt_AC=[0]*N
for i in range(1,N):
    cnt_AC[i]=cnt_AC[i-1]
    if S[i]=='C':
        if S[i-1]=='A':
            cnt_AC[i]+=1

for i in range(Q):
    ans=cnt_AC[R[i]]-cnt_AC[L[i]]
    print(ans)