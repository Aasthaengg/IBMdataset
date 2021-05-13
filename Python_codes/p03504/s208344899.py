# チャンネルの情報は不要ではない, その情報を適切に使う必要がある
from itertools import accumulate
from collections import defaultdict
N, V = map(int, input().split())  # N個の録画したい番組, V個のチャンネル
programs = defaultdict(list)
for _ in range(N):
    s, t, c = map(int, input().split())
    programs[c].append((s, t))

imos = [0] * (100002)
for c, p in programs.items():  # cはチャンネルの番号, pは番組の開始と終了のペアのリスト
    p.sort()  # 開始時間が早い順にソート
    ps, pt = p[0]  # そのチャンネルで一番早い時間に始まる番組の開始と終了の時刻
    for s, t in p[1:]:
        if pt == s:  # もし直前の番組の終了時刻と今から始まる番組の開始時間が一緒なら繋げることができる
            pt = t
        else:
            # 繋げることができない場合、imos法を適用してpsとptを最新のものに変更する
            imos[ps-1] += 1  # ps-0.5を含むからps-1をインクリメントする？
            imos[pt] -= 1  # ptは含まないからptをデクリメントする
            ps, pt = s, t

    # forループでは最後の番組の録画を行っていないのでその処理
    imos[ps-1] += 1
    imos[pt] -= 1

print(max(accumulate(imos)))
