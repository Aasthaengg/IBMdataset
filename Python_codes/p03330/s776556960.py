N,C = map(int, input().split())
D = [[int(d) for d in input().split()] for _ in range(C)]
clist = [[int(c) for c in input().split()] for _ in range(N)]

L0 = [0]*C
L1 = [0]*C
L2 = [0]*C

for i in range(N):
    for j in range(N):
        if (i+j+2)%3 == 0:
            L0[clist[i][j]-1] += 1
        elif (i+j+2)%3 == 1:
            L1[clist[i][j]-1] += 1
        else:
            L2[clist[i][j]-1] += 1
            
ans = 10**9
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i != j and j != k and k != i:
                c = 0
                for l in range(C):
                    c += L0[l]*D[l][i]
                    c += L1[l]*D[l][j]
                    c += L2[l]*D[l][k]
                ans = min(ans, c)
                
print(ans)