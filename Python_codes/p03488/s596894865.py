def main():
    s = input().split('T')
    x, y = map(int, input().split())

    # x軸方向の移動について
    # 1回目の移動はxの正方向のみ
    here_x = [len(s[0])]

    for i in s[2::2]:
        move = len(i)
        here_x = [i + move for i in here_x] + [i - move for i in here_x]
        here_x = set(here_x)

    # y軸方向の移動について
    here_y = [0]

    for i in s[1::2]:
        move = len(i)
        here_y = [i + move for i in here_y] + [i - move for i in here_y]
        here_y = set(here_y)

    if x in here_x and y in here_y:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()