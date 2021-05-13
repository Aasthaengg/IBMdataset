N = int(input())
T = list(map(int, input().split()))
M = int(input())
D = [tuple(map(int, input().split())) for _ in range(M)]

S = sum(T)

for i in range(M):
    print(S - T[D[i][0] - 1] + D[i][1])