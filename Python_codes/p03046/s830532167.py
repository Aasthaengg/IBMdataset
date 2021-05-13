M, K = map(int, input().split())

if K >= 2 ** M:
    print(-1)
    exit()

if K == 0:
    a = []
    for i in range(2 ** M):
        a.append(i)
        a.append(i)
    print(*a)
    exit()

if M == 1 and K == 1:
    print(-1)
    exit()

a = []
a.append(K)
for i in range(2 ** M):
    if i == K:
        continue
    a.append(i)
a.append(K)
for i in range(2 ** M - 1, -1, -1):
    if i == K:
        continue
    a.append(i)
print(*a)
