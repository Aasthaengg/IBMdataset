N, M = map(int,input().split())
ll = [list(map(int,input().split())) for j in range(M)]

a = [0]*N
b = [0]*N

for i in range(M):
    if ll[i][0] == 1:
        a[ll[i][1]-1] += 1
    if ll[i][1] == N:
        b[ll[i][0]-1] += 1

for i in range(N):
    if a[i] != 0 and b[i] != 0:
        print("POSSIBLE")
        exit()
    else:
        pass
print("IMPOSSIBLE")
