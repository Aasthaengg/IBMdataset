N,M = map(int,input().split())
cntNode = [0]*N
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    cntNode[a] += 1
    cntNode[b] += 1

flag = True
for i in range(N):
    if(cntNode[i] % 2 != 0):
        flag = False
        break
if(flag):
    print('YES')
else:
    print('NO')