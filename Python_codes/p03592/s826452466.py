import sys

N, M, K = map(int, input().split())

for n in range(N+1):
    for m in range(M+1):
        if N*m + M*n - n*m*2 == K:
            print("Yes")
            sys.exit()

print("No") 