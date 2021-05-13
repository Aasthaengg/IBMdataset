N,M=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(M)]
num=[0 for i in range(N)]
for i in range(M):
    num[ab[i][0]-1]+=1
    num[ab[i][1]-1]+=1

for i in range(N):
    print(num[i])
