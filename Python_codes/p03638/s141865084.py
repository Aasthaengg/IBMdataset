def d_grid_coloring():
    H, W = [int(i) for i in input().split()]
    N = int(input())
    A = [int(i) for i in input().split()]

    # 方針: 数字を「うなぎ」のように並べればそれが条件を満たす
    # a) 1から順にその数字をそれで塗る回数だけ書き込む
    # b) W 個ごとに分割し，奇数番目は逆にする
    tmp = []
    for k, a in enumerate(A, 1):
        tmp.extend([k] * a)
    ans = [tmp[r * W:(r + 1) * W][::(-1)**r] for r in range(H)]
    return '\n'.join(' '.join(map(str, row)) for row in ans)

print(d_grid_coloring())