N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]
T.insert(0, 0)

for PX in PX:
    ans = T[:]
    ans[PX[0]] = PX[1]
    print(sum(ans))