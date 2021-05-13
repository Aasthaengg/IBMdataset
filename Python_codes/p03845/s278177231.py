N = int(input())
T = list(map(int,input().split()))
M = int(input())
PX = [list(map(int,input().split())) for _ in range(M)]
TSUM = sum(T)
for px in PX:
    print(TSUM + px[1] - T[px[0]-1])