from itertools import product

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def has_neighbor(_i: int, _j: int) -> bool:
    patterns = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
    ]
    cnt = 0
    for pattern in patterns:
        y, x = _i + pattern[0], _j + pattern[1]
        if y in range(H) and x in range(W):
            c = S[y][x]
            if c == "#":
                cnt += 1
        else:
            pass
    if cnt:
        return True
    else:
        return False


for i, j in product(range(H), range(W)):
    if S[i][j] == "#" and not has_neighbor(i, j):
        print("No")
        break
else:
    print("Yes")
