N,M = [int(i) for i in input().split()]
A,B = [],[]
for i in range(N):
    x = [int(i) for i in input().split()]
    A.append(x)
for i in range(M):
    x = [int(i) for i in input().split()]
    B.append(x)

for i in range(N):
    for j in range(M):
        dis = abs(A[i][0] - B[j][0]) + abs(A[i][1] - B[j][1])
        if j == 0:
            min = dis
            tmp = j
        else:
            if dis < min:
                min = dis
                tmp = j
    print(tmp+1)
