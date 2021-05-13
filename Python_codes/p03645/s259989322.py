N,M=map(int,input().split())
E=[[False,False] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())

    if a==1:
        E[b][0]=True

    if b==N:
        E[a][1]=True

F=False
for n in range(1,N+1):
    F|=(E[n][0]&E[n][1])

if F:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
    
