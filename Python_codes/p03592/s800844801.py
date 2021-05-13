import sys

N, M, K = map(int, sys.stdin.readline().split())

# 組み合わせは関係ないため、全探索可能
for i in range(N+1):
    tmp = i * M
    for j in range(M+1):
        tmp += (N - 2 * i)
        if tmp == K:
            print("Yes")
            sys.exit()

print("No")