N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 街iを訪れたらvis[i-1]を0から1にする
visited = [0] * N
# １からスタートして、訪れる街を順に記録
a = []
# １からスタート
town = 1

# 街pをまだ訪れていない場合
while visited[town - 1] == 0:
    # pを訪れたことを記録
    visited[town - 1] = 1
    # pを訪れた順番を記録
    a.append(town)
    # テレポート先はA[p-1]
    town = A[town - 1]

# ここでtownはループの先頭の町の番号
loop_head = a.index(town)

# K==len(a)-1だとちょうどaの最後で止まる
# Kがlen(a)以上だとループに入る
if K < len(a):
    print(a[K])
else:
    # ループに入る前までに移動回数をloop_head消費する
    # ループの長さはlen(a) - loop_head
    K -= loop_head
    print(a[loop_head + K % (len(a) - loop_head)])
