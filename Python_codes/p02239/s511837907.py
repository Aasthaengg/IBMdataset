N=int(input())
List = [[] for i in range(N+1)]
for i in range(N):
    l=list(map(int,input().split()))
    List[l[0]]=l[2:]
#print(List)
D=[10**9 for i in range(N+1)]

Q=[[0,1]]
for i in range(10**9):
    if len(Q)==i:
        break
    if D[Q[i][1]]==10**9:
        D[Q[i][1]]=Q[i][0]
        for j in List[Q[i][1]]:
            if D[j]==10**9:
                Q.append([Q[i][0]+1,j])
for i in range(1,N+1):
    if D[i]==10**9:
        print(i,-1)
    else:
        print(i,D[i])
