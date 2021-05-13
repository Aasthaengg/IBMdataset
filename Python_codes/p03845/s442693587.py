N = int(input())
T = [int(i) for i in input().split()]
M = int(input())
PX = [[int(i) for i in input().split()] for i in range(M)]

for i in range(M):
    ans = sum(T) - T[PX[i][0] - 1] + PX[i][1]
    print(ans)
