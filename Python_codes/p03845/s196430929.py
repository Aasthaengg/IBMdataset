N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for i in range(M)]

for i in range(M):
    test = []
    for j in range(N):
        test.append(T[j])
    test[PX[i][0]-1] = PX[i][1]
    print(sum(test))
