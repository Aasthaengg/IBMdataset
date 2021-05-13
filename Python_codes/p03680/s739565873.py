N = int(input())
A = [int(input()) for _ in range(N)]

i = 0

for n in range(N):
    i = A[i] - 1
    if i == 1:
        print(n + 1)
        exit()

print(-1)