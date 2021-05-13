N, M = map(int, input().split())
S = input()


# 後ろから貪欲
ans = []
position = N
while position > 0:
    for move in range(M, 0, -1):
        if position - move < 0:
            continue

        if S[position - move] == '1':
            continue

        ans.append(move)
        position -= move
        break
    else:
        print(-1)
        exit()

print(*ans[::-1])
