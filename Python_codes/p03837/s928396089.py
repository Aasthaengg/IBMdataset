import sys

input=sys.stdin.readline

N,M=map(int,input().split())
hen=[]
for i in range(0,M):
    a,b,length=map(int,input().split())
    hen.append((a-1,b-1,length))

shortest=[[10**20 for i in range(0,N)] for j in range(0,N)]

for i in range(0,M):
    a,b,length=hen[i]
    shortest[a][b]=length
    shortest[b][a]=length

for k in range(0,N):
    for i in range(0,N):
        for j in range(0,N):
            shortest[i][j]=min(shortest[i][j],shortest[i][k]+shortest[k][j])

count=0
for i in range(0,M):
    a,b,length=hen[i]
    if length!=shortest[a][b]:
        count+=1

print(count)