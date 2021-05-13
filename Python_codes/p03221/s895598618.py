N, M = map(int, input().split())

# (Pi,Yi)のようなタプルの形で保存する
# Yiでソートしたいので、別のリストで管理するのは非効率
PY = []

# keyはYi、valueはi
# i順に出力するためのメモ用辞書
Y_to_i = dict()

for i in range(M):
    p, y = map(int, input().split())
    # タプルは後で変更できない（良く言えば「保持される」）
    PY.append((p, y))
    # yに対するiを記録、ここでyはuniqueであることが問題で保証されている
    Y_to_i[y] = i

# 第一引数(=県の番号)で大雑把にソート、同じ県内では、第二引数(=誕生年)で細かくソート
PY.sort()

ID_list = [""] * M

temp_p = PY[0][0]

idx = 1

for p, y in PY:

    # 県が変わったらidxは1に初期化
    if p != temp_p:
        idx = 1

    # 上のifをやるために現在のpをtemp_pとして記録しておく
    temp_p = p

    # ID_listには、最初に受け取った「市の番号」順に結果を格納
    ID_list[Y_to_i[y]] = str(p).zfill(6) + str(idx).zfill(6)

    # 次のためにidxをincrement
    idx += 1

# 市の番号順に入っているのでそのまま出力するだけ
for a in ID_list:
    print(a)
