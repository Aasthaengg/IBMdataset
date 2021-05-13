N=int(input())
A=[[] for _ in range(N)]

for i in range(N):
    A[i]=list(map(int,input().split()))

NE=[0]*N#i番目の人が，次何番目の試合をするかのリスト
F=[0]*N#i番目の人が，該当する日に試合をしたか記憶しておく

#i+1日目の試合をする人はi日目に試合をした人なので，それを2つのqueueに記憶．
Q=[[],[]]

#初日
for i in range(N):
    opp=A[i][0]-1
    if A[opp][0]-1==i:
        NE[i]+=1
        Q[0].append(i)

ans=1
#d日目
for d in range(N*(N-1)//2):
    F=[0]*N
    a=d%2
    b=(d+1)%2
    while len(Q[a])!=0:
        i=Q[a].pop()
        if NE[i]==N-1:
            continue
        opp=A[i][NE[i]]-1
        if F[i]==1 or F[opp]==1:#その日に試合したことがある人はスルー,oppの重複防止
            continue
        if A[opp][NE[opp]]-1==i:
            NE[i]+=1
            NE[opp]+=1
            F[i]=1
            F[opp]=1
            if NE[i]!=N-1:
                Q[b].append(i)
            if NE[opp]!=N-1:
                Q[b].append(opp)
    ans+=1
    if len(Q[a])==0 and len(Q[b])==0:
        break

for i in range(N):
    if NE[i]!=N-1:
        ans=-1
print(ans)