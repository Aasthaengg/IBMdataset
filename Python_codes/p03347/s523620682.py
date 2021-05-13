N = int(input())
A = [int(input()) for i in range(N)]

if A[0] != 0:
    print(-1)
    exit()

for i in range(N - 1):
    if A[i] < A[i + 1] and A[i + 1] - A[i] != 1:
        print(-1)
        exit()
    if A[i] > i + 1:
        print(-1)
        exit()

ans = 0
i = 1
old = 0
while i != N:
    if A[i] <= old:
        ans += old
    old = A[i]
    i += 1

print(ans + A[-1])
