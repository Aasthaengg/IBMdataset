def d_crossing(N):
    """
    S_k は、どの2つの部分集合の共通部分の要素数が1であり、1からNのどの要素も
    ちょうど2回しか使われないため、各集合の要素数はいずれもk-1である。
    また、要素数の和を考えると、 2N=k(k-1) ⇔ N=k(k-1)/2 である。

    逆に、1からk(k-1)/2までの数を三角形に並べたあと、対称行列になるように
    行列を構成すると、各行(列でも可)または対角成分を要素とした集合を部分集合とすれば
    条件を満たせる。
    (例: N=6)
    1         1 2 4
    2 3   <=> 2 3 5
    4 5 6     4 5 6
    として、{1, 2, 4}, {2, 3, 5}, {4, 5, 6}, {1, 3, 6} を部分集合とすればよい。
    """

    # N = k(k-1)/2 となる正整数kが存在するなら、求めるものが作れる
    k = 2
    while True:
        tmp = k * (k - 1)
        if tmp > 2 * N:
            return 'No'
        elif tmp == 2 * N:
            ans = ['Yes']
            break
        k += 1

    ans.append(str(k))
    # 1からk(k-1)/2までの数を三角形に並べ、対称行列を構成する
    matrix = [[0] * (k - 1) for _ in range(k - 1)]
    cnt = 1
    for r in range(k - 1):
        for c in range(r + 1):
            matrix[c][r] = matrix[r][c] = cnt
            cnt += 1
    # 各行を取り出したものを部分集合とする
    for r in matrix:
        ans.append('{0} {1}'.format(k - 1, ' '.join(map(str, r))))
    # 対角成分を取り出したものを部分集合とする
    tmp = [matrix[j][j] for j in range(k - 1)]
    ans.append('{0} {1}'.format(k - 1, ' '.join(map(str, tmp))))
    # 出力形式に沿って出力
    ans = '\n'.join(ans)
    return ans

N = int(input())
print(d_crossing(N))