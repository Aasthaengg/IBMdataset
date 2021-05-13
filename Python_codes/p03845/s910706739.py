N = int(input())
T = [int(i) for i in input().split()]
M = int(input())
px = [[int(i) for i in input().split()] for j in range(M)]

for i in range(M):
    dt = T[px[i][0]-1] - px[i][1]
    print(sum(T) - dt)