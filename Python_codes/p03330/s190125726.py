N,C = map(int,input().split())

D = [[0]*C for i in range(C)]

for i in range(C):
    D[i] = list(map(int,input().split()))

c = [0 for i in range(N)]

for i in range(N):
    c[i] = list(map(int,input().split()))
    for j in range(N):
        c[i][j] -= 1
#print(c)

differ = [[0]*C for i in range(3)]
###differ[i][j] (x+y)%3==i　となるようなマス全ての色をCにした時の違和感の合計

for i in range(N):
    for j in range(N):
        for k in range(C): 
            differ[(i+j)%3][k] += D[c[i][j]][k]

ans = 25 *(10**7)

for i in range(C):
    for j in range(C):
        for k in range(C):
            if i==j or j==k or k==i:
                continue
            ans = min(ans,differ[0][i]+differ[1][j]+differ[2][k])
            #print(i,j,k,ans)

print(ans)