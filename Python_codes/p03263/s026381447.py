H, W = map(int, input().split())

a = [[-1]*(W+2) for _ in range(H+2)]
odd_count = 0

for i in range(1, H+1):
    tmp = list(map(int, input().split()))
    for j in range(1, W+1):
        a[i][j] = tmp[j-1]
        odd_count += int(a[i][j] % 2 == 1)

moves = []
# 一筆書きの経路を作成
routes = []
for h in range(1, H+1):
    tmp = []
    for w in range(1, W+1):
        tmp.append((h, w))
    if h % 2 == 1:
        routes += tmp
    else:
        routes += tmp[::-1]

is_carrying = 0
for i, (h, w) in enumerate(routes):
    if i == H*W-1:
        break
    if odd_count == 1:
        break
    if a[h][w] % 2 == 1 and not is_carrying:
        tmp = (h, w)
        is_carrying = 1
        moves.append((h, w, routes[i+1][0], routes[i+1][1]))
    elif a[h][w] % 2 == 1 and is_carrying:
        is_carrying = 0
        odd_count -= 2
        
    elif a[h][w] % 2 == 0 and is_carrying:
        moves.append((h, w, routes[i+1][0], routes[i+1][1]))

print(len(moves))
for move in moves:
    print(*move)