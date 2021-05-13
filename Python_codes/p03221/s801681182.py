import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()
city = [[] for i in range(N+1)]
for i in range(M):
    P,Y = MI()
    city[P].append((Y,i))

ID = []
for i in range(N+1):
    city[i] = sorted(city[i])
    for j in range(len(city[i])):
        P,Y = city[i][j]
        ID.append((Y,str(i).zfill(6)+str(j+1).zfill(6)))

ID.sort()
for i in range(M):
    print(ID[i][1])
