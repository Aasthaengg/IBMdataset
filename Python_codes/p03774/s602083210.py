N,M = map(int,input().split())
students = [list(map(int,input().split()))for i in range(N)]
checkPoints = [list(map(int,input().split()))for i in range(M)]

for i in range(N):
    idx = 1
    mindis = abs(students[i][0]-checkPoints[0][0])+ abs(students[i][1]-checkPoints[0][1])
    sx,sy = students[i]
    for j in range(1,M):
        cx,cy = checkPoints[j]
        distance = abs(sx-cx)+ abs(sy-cy)
        if mindis > distance:
            idx = j+1
            mindis = distance
    print(idx)

