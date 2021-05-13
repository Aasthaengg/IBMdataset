N = int(input())
lsT = list(map(int,input().split()))
M = int(input())
sum1 = sum(lsT)
lsP = []
for i in range(M):
    lsP.append(list(map(int,input().split())))

for i in range(M):
    print(sum1-lsT[lsP[i][0]-1]+lsP[i][1])