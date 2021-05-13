N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

S  = sum(T)
for p, x in PX:
    print(S - T[p - 1] + x)