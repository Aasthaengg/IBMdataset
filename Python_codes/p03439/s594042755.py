def func(l, r, same) -> int:
    """
    X(l,r)X -> same=True
    X(l,r)y -> same=False
    次の送信クエリ候補を返す
    """
    parity = (r - l + 1) % 2
    if parity ^ same:
        ret = (l + r) // 2
    else:
        ret = -1
    return ret


def main():
    n = int(input())

    seat = [''] * n

    print(0, flush=True)
    response = input()
    if response[0] == 'V':
        print(0)
        return
    seat[0] = response[0]

    l, r = 0, n
    x = func(l, r, same=True)
    for _ in range(19):
        print(x, flush=True)
        response = input()
        if response[0] == 'V':
            print(x)
            return
        seat[x] = response[0]

        res = func(l, x, seat[l] == seat[x])
        if res != -1:
            r = x
            x = res
            continue

        res = func(x, r, seat[x] == seat[r % n])
        if res != -1:
            l = x
            x = res


if __name__ == '__main__':
    main()
