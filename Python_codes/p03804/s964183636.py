N,M = map(int,input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]
ans = False

for ly in range(N):
    for lx in range(N):
        if N - M + 1 <= lx:
            continue
        if N - M + 1 <= ly:
            continue
        flag = True
        for y in range(M):
            for x in range(M):
                if B[y][x] != A[ly+y][lx+x]:
                    flag = False
        if flag:
            ans = True

print('Yes' if ans else 'No')