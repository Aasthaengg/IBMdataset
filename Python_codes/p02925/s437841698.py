N = int(input())
A = []
for _ in range(N):
    A.append([x - 1 for x in map(int, input().split())])

game = []
for p1 in range(N):
    p2 = A[p1][0]
    if A[p2][0] == p1 and p1 < p2:
        game.append((p1, p2))

cursors = [0] * N
days = 0
while game:
    days += 1
    new_game = []
    for p1, p2 in game:
        cursors[p1] += 1
        if cursors[p1] < N - 1:
            p3 = A[p1][cursors[p1]]
            if cursors[p3] < N - 1 and A[p3][cursors[p3]] == p1:
                new_game.append((p1, p3))
        cursors[p2] += 1
        if cursors[p2] < N - 1:
            p3 = A[p2][cursors[p2]]
            if cursors[p3] < N - 1 and A[p3][cursors[p3]] == p2:
                new_game.append((p2, p3))
    game = new_game

if all(c == N - 1 for c in cursors):
    print(days)
else:
    print(-1)