# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N, M = list(map(int, input().split()))
    k, s = [], []
    for m in range(M):
        l = list(map(int, input().split()))
        k.append(l[0])
        s.append(l[1:])
    p = list(map(int, input().split()))

    return N, M, k, s, p


def main(N: int, M: int, s: list, p: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): スイッチの数(1 <= N <= 10)
        M (int): 電球の数(1 <= M <= 10)
        s (list): 電球と繋がっているスイッチ(1 <= s_ij <= N)
        p (list): 点灯判定(0または1)
    """
    # 求解処理
    ans = 0
    for bit in range(1 << N):
        is_all_light_on = True
        for m in range(M):
            on_count = 0
            for s_i in s[m]:
                if ((bit >> (s_i - 1)) & 1):
                    on_count += 1
            if on_count % 2 != p[m]:
                is_all_light_on = False
                break
        if is_all_light_on:
            ans += 1

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, M, k, s, p = get_input()

    # メイン処理
    main(N, M, s, p)
