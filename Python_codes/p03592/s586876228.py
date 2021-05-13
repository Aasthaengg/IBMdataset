import sys
N, M, K = map(int, input().split())

for i in range(0, N+1):
    for j in range(0, M+1):
        ans = (M * i) + (N * j) - 2 * (i * j)
        if ans == K:
            print("Yes")
            sys.exit()
print("No")