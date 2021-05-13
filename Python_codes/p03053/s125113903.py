H,W = map(int,input().split())
lis = [[1000000007] * W for i in range(H)]
A = []
for i in range(H):
    Ain = list(input())
    A.append(Ain)
    for j in range(W):
        if A[i][j] == '#':
            lis[i][j] = 0
        else:
            lis[i][j] = min(lis[i][j],lis[i][j-1]+1)

    for j in reversed(range(W-1)):
        lis[i][j] = min(lis[i][j],lis[i][j+1]+1)
#print(lis)

for j in range(W):
    for i in range(1,H):
        lis[i][j] = min(lis[i][j],lis[i-1][j]+1)
    for i in reversed(range(H-1)):
        lis[i][j] = min(lis[i][j],lis[i+1][j]+1)

#print(lis)
ans = 0
for i in range(H):
    ans = max(ans,max(lis[i]))
print(ans)
