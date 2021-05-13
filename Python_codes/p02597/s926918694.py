#!/usr/bin/env python3


def main():
    n = int(input())
    s = input()
    # print("s: " + s)
    # 左に白が存在する赤
    # 右に赤が存在する白 <=> これらは交換しても良い
    # minimumな個数を交換すればいいはず
    # 塗り替えは実はする必要はない
    w = 0
    r = 0
    for i in range(len(s)):
        if s[i] == 'R':
            r += 1
    # print(len(s))
    # print(str(w) + " " + str(r))

    res_min = r
    for i in range(1, len(s) + 1):
        if s[i-1] == 'R':
            r -= 1
        elif s[i-1] == 'W':
            w += 1

        res_min = min(res_min, max(w, r))

    print(res_min)


if __name__ == '__main__':
    main()
