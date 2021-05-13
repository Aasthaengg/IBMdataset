H, W, K = list(map(int, input().split(' ')))
# mat[i][j] = mat[i-1][j-1] * hoge + mat[i-1][j-1] * fuga + mat[i+1][j-1] * piyo
# hoge, fuga, piyo は隣接していない自由に置いて良い | | | ... | で固定値で決まる
# |-| -> hoge(2)=2
# |-|-| -> hoge(3)=3
# |-|-|-| -> hoge(4)=5
# |-|-|-|-| -> hoge(5)=8
# |-|-|-|-|-| -> hoge(6)=13
# |-|-|-|-|-|-| -> hoge(7)=21?
mat = []
for i in range(H+1):
    mat.append([0] * (W))
mat[0][0] = 1

def get(h, w):
    if h < 0 or w < 0:
        return 0
    if h >= H or w >= W:
        return 0
    return mat[h][w]

def hoge(w):
    d={1:1, 2:2, 3:3, 4:5, 5:8, 6:13, 7:21}
    return d.get(w, 1)

for i in range(1,H+1):
    for j in range(W):
        mat[i][j] = get(i-1, j-1) * hoge(j-1) * hoge(W-j-1) +\
                    get(i-1, j)   * hoge(j)   * hoge(W-j-1) +\
                    get(i-1, j+1) * hoge(j)   * hoge(W-j-1-1)
print(mat[H][K-1] % 1000000007)