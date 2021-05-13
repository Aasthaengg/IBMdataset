# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]

    # スターグラフを作ってみる
    for i in range(m):
        ai, bi = map(int, input().split())
        # 0-index
        ai -= 1
        bi -= 1

        if ai == 0:
            a[bi] += 1
        elif bi == 0:
            b[ai] += 1
        else:
            a[bi] += 1
            b[ai] += 1

    for ai, bi in zip(a, b):
        if (ai + bi) % 2 == 1:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
