def z_algo(s):
    """https://www.youtube.com/watch?v=f6ct5PQHqM0
    """
    n = len(s)
    ret = [0] * n

    ref_frm, ref_tail = -1, -1  # 一番末尾まで探索したケースの起点と終点
    for frm in range(1, n):
        cont = max(0, min(ret[frm - ref_frm], ref_tail - frm)) if ~ref_frm else 0

        while (frm + cont < n) and (s[cont] == s[frm + cont]): cont += 1
        ret[frm] = cont
        if ref_tail < frm + cont:
            ref_tail = frm + cont
            ref_frm = frm
    ret[0] = n
    return ret


def main():
    N = int(input())
    S = input()

    ret = 0
    t = ''
    for c in reversed(S):
        # zalgoは[0,i]の比較で
        # 先頭が固定されているので
        # 末尾から文字を増やしていくことで
        # 先頭をSの各文字にしている
        t = c + t
        lcp = z_algo(t)
        for diff, len_ in enumerate(lcp):
            ret = max(ret, min(diff, len_))
    print(ret)


if __name__ == '__main__':
    main()
