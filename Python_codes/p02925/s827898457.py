from collections import deque, defaultdict

N = int(input())
A = [deque(map(lambda a: int(a) - 1, input().split())) for _ in range(N)]

D = [0] * N
canBattle = defaultdict(lambda: False)
que = deque(range(N))

while que:
    i = que.popleft()
    j = A[i][0]
    canBattle[(i, j)] = True

    if canBattle[(j, i)]:
        A[i].popleft()
        A[j].popleft()
        day = max(D[i], D[j])
        D[i] = D[j] = day + 1

        if A[i]:
            que.append(i)
        if A[j]:
            que.append(j)

if all(len(a) == 0 for a in A):
    print(max(D))
else:
    print(-1)


