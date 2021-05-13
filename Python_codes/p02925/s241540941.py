N=int(input())
A=[[] for i in range(0,N)]
nodes=[]
for i in range(0,N-1):
    for j in range(i+1,N):
        nodes.append((i,j))

order={i:[0 for j in range(0,N)] for i in range(0,N)}
for i in range(0,N):
    A[i]=list(map(int,input().split()))
    for j in range(0,N-1):
        order[i][A[i][j]-1]=j
        #i番目の人がj番目の人と戦うのが何番目か


q=set([])
for battle in nodes:
    i,j=battle
    if order[i][j]==0 and order[j][i]==0:
        q.add(battle)

flag=[0 for i in range(0,N)]

day=0
sub=set([])
while q:
    while q:
        i,j=q.pop()
        flag[i]+=1
        flag[j]+=1
        if flag[i]!=N-1:
            s=A[i][order[i][j]+1]-1
            if flag[s]>=order[s][i]:
                sub.add((i,s))
        if flag[j]!=N-1:
            t=A[j][order[j][i]+1]-1
            if flag[t]>=order[t][j]:
                sub.add((j,t))

        if not q:
            day+=1
            q=sub
            sub=set([])
            break

able=True
for i in range(0,N):
    if flag[i]!=N-1:
        able=False

if able:
    print(day)
else:
    print(-1)