def get_move(S):
    S = S.split("T")
    x_move = [len(x) for x in S[0::2]]
    y_move = [len(x) for x in S[1::2]]
    return x_move, y_move


def check(x, move):
    move.sort()
    while move:
        m = move.pop()
        if x >= 0:
            x -= m
        else:
            x += m
    return x == 0


if __name__ == "__main__":
    S = input()
    x, y = map(int, input().split())

    x_move, y_move = get_move(S)
    # 初手正方向に移動
    x -= x_move[0]

    if check(x, x_move[1:]) and check(y, y_move):
        ans = "Yes"
    else:
        ans = "No"

    print(ans)
