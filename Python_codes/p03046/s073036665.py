M, K = map(int,input().split())
if [M, K] == [0, 0]:
    print("0 0")
    exit(0)
if [M, K] == [1, 0]:
    print("0 0 1 1")
    exit(0)
if [M, K] == [1, 1]:
    print(-1)
    exit(0)
if 2**M <= K:
    print(-1)
    exit(0)

a = []
for k in range(2**M):
    if k != K:
        a.append(k)
ans = a+[K]+a[::-1]+[K]
print(*ans, sep=" ")