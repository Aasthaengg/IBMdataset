import sys

N, K = map(int, sys.stdin.readline().split())

comb = (N-1) * (N-2) // 2

if K > comb:
    print(-1)
else:
    # print("comb", comb, "K", K)
    res = comb - K
    print(N-1 + res)
    for i in range(2, N+1):
        print(1, i)
    for i in range(2, N):
        for j in range(i, N):
            if res == 0:
                sys.exit()
            print(i, j+1)
            res -= 1