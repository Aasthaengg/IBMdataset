N=int(input())

G=[[] for i in range(N+1)]

if N%2==0:
    S=N+1
else:
    S=N

cnt=0

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if i+j != S:
            G[i].append(j)
            cnt+=1

print(cnt)
for i in range(1,N+1):
    for j in range(len(G[i])):
        print(i,G[i][j])
