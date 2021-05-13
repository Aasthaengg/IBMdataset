N,M = list(map(int,input().split()))

ship={}
for n in range(N):
    n=n+1
    ship[n]=[]

for m in range(M):
    a,b=list(map(int,input().split()))
    if a == 1:
        ship[a].append(b)
    else :
        if b == N:
            ship[a].append(b)

ans='IMPOSSIBLE'
for i in ship[1]:
    if len(ship[i]) != 0:
        ans='POSSIBLE'
        break
print(ans)