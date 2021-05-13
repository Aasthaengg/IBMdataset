A, B, K = map(int, input().split())
M = min(A, B)

cnt = 0
for i in range(M):
    if A%(M-i) == 0 and B%(M-i) == 0:
        cnt += 1
        if cnt == K:
            print(M-i)
            break