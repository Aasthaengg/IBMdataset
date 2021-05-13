#!/usr/bin/env python3

import sys


def main():
    def input(): return sys.stdin.readline().rstrip()
    def mi():    return map(int, input().split())
    def lmi():   return list(map(int, input().split()))

    def move(from_i, from_j, to_i, to_j, ans):
        y, x = from_i, from_j
        while not (y == to_i and x == to_j):
            # print(f"{y} {x} {to_i} {to_j}")
            if (y % 2 == 0 and x == w - 1) or (y % 2 == 1 and x == 0):
                # 下へ
                ans.append("{} {} {} {}".format(y+1, x+1, y+2, x+1))
                y += 1
            elif y % 2 == 0:
                # 右へ
                ans.append("{} {} {} {}".format(y+1, x+1, y+1, x+2))
                x += 1
            else:
                # 左へ
                ans.append("{} {} {} {}".format(y+1, x+1, y+1, x))
                x -= 1
    
    h, w = mi()
    L = [lmi() for _ in range(h)]
    coin_odd = []
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                if L[i][j] % 2 == 1:
                    coin_odd.append((i, j))
        else:
            for j in range(w-1, -1, -1):
                if L[i][j] % 2 == 1:
                    coin_odd.append((i, j))              

    ans = []
    # 偶数コインが置かれた、っていう表現は 0 枚を含まないと思うのですが...
    # 質問によると含むらしい。それなら実装はかなり単純
    coin_odd.reverse()
    # print(coin_odd)
    while len(coin_odd) >= 2:
        from_i, from_j = coin_odd.pop()
        to_i, to_j = coin_odd.pop()
        move(from_i, from_j, to_i, to_j, ans)
        L[from_i][from_j] -= 1
        L[to_i][to_j] += 1

    print(len(ans))
    for line in ans:
        print(line)
    
    # for l in L:
    #     print(*l)


if __name__ == "__main__":
    main()
