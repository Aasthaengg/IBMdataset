N, M = [int(i) for i in input().split()]

cnt = 0

if N  <= M // 2:
    cnt = N
    M = M - (2 * N)
    N = 0
    cnt += M // 4
else :
    cnt = M // 2
print(cnt)