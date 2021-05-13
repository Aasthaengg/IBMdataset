def judge(c):
    if len(c) == 0:
        return 1, c, "-1"
    else:
        return 0, c[0], c[1:]


def main():
    sa = input()
    sb = input()
    sc = input()
    card = {"a": sa, "b": sb, "c": sc}
    next_player = "a"
    while True:
        now = next_player
        is_finish, next_player, card[now] = judge(card[now])
        if is_finish:
            print(now.upper())
            break


if __name__ == '__main__':
    main()

