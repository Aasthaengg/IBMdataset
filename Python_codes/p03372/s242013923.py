N,C = map(int,input().split())
XV = [list(map(int,input().split())) for i in range(N)]

migiM = [0]
tmp = 0
for i in range(N):
    tmp =  tmp + XV[i][1]
    migiM.append(max(migiM[-1],tmp-XV[i][0]))

hidariM = [0]
tmp = 0
for i in range(N):
    tmp =  tmp + XV[N-i-1][1]
    hidariM.append(max(hidariM[-1],tmp-C+XV[N-i-1][0]))
    
ans = max(migiM[N],hidariM[N])
tmp = 0
for i in range(N):
    tmp = tmp + XV[i][1]
    if ans < tmp + hidariM[N-1-i] - 2*XV[i][0]:
        ans = tmp + hidariM[N-1-i] - 2*XV[i][0]
        
tmp = 0
for i in range(N):
    tmp = tmp + XV[N-1-i][1]
    if ans < tmp + migiM[N-1-i]  - 2*(C-XV[N-1-i][0]):
        ans = tmp + migiM[N-1-i] - 2*(C-XV[N-1-i][0])

#print(migiM,hidariM)
print(ans)