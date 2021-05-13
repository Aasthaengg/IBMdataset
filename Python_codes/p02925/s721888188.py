N = int(input())
A = [list(map(lambda x: int(x) - 1, input().split())) + [-1] for i in range(N)]

ans = 0
matched = 0
marker = [0] * N
que = list(range(N))

while matched < N * (N - 1) // 2:
    already_matched = set()
    next_que = []

    while que:
        player = que.pop()
        partner = A[player][marker[player]]

        if A[partner][marker[partner]] == player:
            if not ((player not in already_matched) and (partner not in already_matched)):
                continue

            matched += 1

            marker[player] += 1
            marker[partner] += 1

            already_matched.add(player)
            already_matched.add(partner)

            next_que.append(player)
            next_que.append(partner)

    if not next_que:
        print(-1)
        break

    ans += 1
    que = next_que[:]

else:
    print(ans)
