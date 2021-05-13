N = int(input())
T = list(map(int, input().split()))
M = int(input())
drag = [list(map(int, input().split())) for n in range(M)]
for d in drag:
    print(sum(T) - T[d[0] - 1] + d[1])