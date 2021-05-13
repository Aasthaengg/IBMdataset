N,C = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(C)]
c = [list(map(int,input().split())) for _ in range(N)]
lis = [[] for _ in range(3)]
#print(lis)
for i in range(N):
    for j in range(N):
        lis[(i+j+2) % 3].append(c[i][j])
#print(lis)
val = [[] for _ in range(3)]
for i in range(3):#lis[i]
    for j in range(C):#d[]
        cnt = 0
        for k in lis[i]:
            #print(k)
            cnt += D[k-1][j]
        val[i].append(cnt)
#print(lis)
#print(val)
ans = float('inf')
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or k == i:
                continue
            ans = min(ans,val[0][i]+val[1][j]+val[2][k])
print(ans)

