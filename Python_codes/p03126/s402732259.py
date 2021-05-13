N,M=map(int,input().split())
KA=[]
food=[N]*M
for i in range(N):
    KA.append(list(map(int,input().split())))
for i in range(N):
    for j in range(len(KA[i])-1):
        food[KA[i][j+1]-1]-=1
print(food.count(0))