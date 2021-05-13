from sys import exit
N, M, K  = map(int, input().split())
if K == 0:
    print("Yes")
    exit()
for n in range(N + 1):
    for m in range(M + 1):
        if (N - n) * (M - m) + n * m == K:
            print("Yes")
            exit()
print("No")