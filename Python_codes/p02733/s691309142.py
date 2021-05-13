from collections import defaultdict
H, W, K = map(int, input().split())  # H行, W列, 1エリア内にK個以下のホワイトチョコレートにしたい
gridgraph = [list(input()) for _ in range(H)]
ans = 10**10
# Hに関するビット全探索を行うイメージ
for i in range(1 << (H-1)):
    bits = []
    for j in range(H-1):
        bits.append((i >> j) & 1)  # iのjビット目が立っているかどうかを調べる
    separate_row = True
    cnt = sum(bits)  # 横に切る場所, 最終的に ans = min(ans, cnt)をする
    all_accumulation = defaultdict(int)
    # その列を区切るか区切らないかを貪欲法で判断していく
    for j in range(W):
        now_area = 0
        now_accumulation = defaultdict(int)
        for i in range(H):
            # iが変動していく
            # 今見ている列のものだけも、数えておく必要がある
            now_accumulation[now_area] += int(gridgraph[i][j])
            if i != H-1:
                now_area += bits[i]
        # その列を見終わったら、cntをインクリメントすることでリセットできる
        if all([K >= v for v in now_accumulation.values()]):
            for key in now_accumulation.keys():
                all_accumulation[key] += now_accumulation[key]
            # 累積されていたものに足した
            if all([K >= v for v in all_accumulation.values()]):
                continue
            else:
                cnt += 1
                # 今見ていたところの左側を分割して、累積部分の値を現在のものに変更する
                all_accumulation = now_accumulation.copy()
        else:
            # その行だけを見てもKを超えるものがあるなら行の分割の仕方が論外
            separate_row = False
            break
    if separate_row:
        ans = min(ans, cnt)
print(ans)
