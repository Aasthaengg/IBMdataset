def Qc():
    """
    塗りつぶされた列をbitに置き換えて探索する
    """
    h, w, k = map(int, input().split())
    lines = [input() for v in range(h)]
    ans = 0
    for ir in range(2 ** h):
        for ic in range(2 ** w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if (ir >> i) & 1 and (ic >> j) & 1:
                        if lines[i][j] == '#':
                            cnt += 1
            if cnt == k:
                ans += 1
    print(ans)


if __name__ == '__main__':
    Qc()
