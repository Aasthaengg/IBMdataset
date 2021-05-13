N,M=map(int,input().split())
S=list(map(int,input().split()))
S.sort()

TRADE=[[0 for j in range(2)] for i in range(M)]

for i in range(M):
    B,C=map(int,input().split())
    TRADE[i][0]=B
    TRADE[i][1]=C


T=sorted(TRADE,key=lambda x:x[1],reverse=True)


TLEN=0
pos=0
flag=True
while TLEN<M and flag==True:
    for i in range(T[TLEN][0]):
        if S[pos]<T[TLEN][1]:
            S[pos]=T[TLEN][1]
            pos+=1
        else:
            flag=False
            break
        if pos>len(S)-1:
            flag=False
            break
    TLEN+=1

print(sum(S))