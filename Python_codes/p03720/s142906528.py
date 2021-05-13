N,M=[int(i) for i in input().split()]
arrR=[0]*N
for m in range(M):
    a,b=[int(i) for i in input().split()]
    arrR[a-1]+=1
    arrR[b-1]+=1
[print(arrR[i]) for i in range(N)]
