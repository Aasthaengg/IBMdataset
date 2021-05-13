N, M = map(int, input().split())

if N % 2 == 0:
    N -= 1

li = []
i, j = 1, (N + 1) // 2
while i < j:
    li.append((i, j))
    i += 1
    j -= 1
i, j = N, (N + 3) // 2
while i > j:
    li.append((j, i))
    i -= 1
    j += 1

for m in range(M):
    print(li[m][0], li[m][1])