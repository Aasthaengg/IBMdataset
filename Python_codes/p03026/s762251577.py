N=int(input())

G=[[] for i in range(N+1)]

for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
C=list(map(int,input().split()))
C.sort(reverse=True)
S=sum(C[1:])

num=[0 for i in range(N+1)]
un_used=[True for i in range(N+1)]

q=[]
q.append(1)
un_used[1]=False

while q:
    node = q.pop(0)
    num[node] = C.pop(0)
    
    for i in range(len(G[node])):
        if un_used[G[node][i]]:
            un_used[G[node][i]]=False
            q.append(G[node][i])

print(S)
print(" ".join(map(str,num[1:])))