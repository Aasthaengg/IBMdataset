N = int(input())
T = [int(t) for t in input().split()]
M = int(input())
PX = [tuple(map(int, input().split())) for _ in range(M)]

total_time = sum(T)
for i in range(M):
    p, x = PX[i]
    print(total_time - T[p - 1] + x)
