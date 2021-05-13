N = int(input())
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N-1):
        temp[j] -= 1
    A.append(temp)

cand = list(range(N))
cur = [0] * N
goal = 0
day = 0
while goal < N:
    day += 1
    game = []
    new_cur = cur[:]
    for i in cand:
        if i in game or cur[i] == N-1:
            continue
        opponent = A[i][cur[i]]
        if A[opponent][cur[opponent]] == i:
            new_cur[i] += 1
            new_cur[opponent] += 1
            game.append(i)
            game.append(opponent)
            if new_cur[i] == N-1:
                goal += 1
            if new_cur[opponent] == N-1:
                goal += 1
    cand = game
    cur = new_cur
    if not game:
        print(-1)
        exit()

print(day)
