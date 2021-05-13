W, B = map(int, input().split())
S = 100

#上半分を白、下半分を黒にする。
# W,B<=500に対し、マップは 100*100=10000 と十分すぎるほど大きい
# これを利用し
# ***************
# * * * * * * * *
# ***************
# * * * * * * * *
# ***************
# と、一行おきに1マスおきに反対の色をおけばいい
# こうしても一行 S // 2 = 50 個配置可能。20行あればOK
# つまり100x100なら十分たりる

#0=white, 1=blackとする。最終的に .# にする
Mij = [[0 for _ in range(S)] for _ in range(S)]
for i in range(S):
    v = 0 if i < S // 2 else 1
    for j in range(S):
        Mij[i][j] = v

# 上に黒配置
count = 1
for i in range(1, S // 2, 2):
    for j in range(0, S, 2):
        if count < B:
            Mij[i][j] = 1
            count += 1
# 下に白配置
count = 1
for i in range(S - 1, S // 2, -2):
    for j in range(0, S, 2):
        if count < W:
            Mij[i][j] = 0
            count += 1

# 出力。白=0=.  /  黒=1=#
print(S, S)
for mi in Mij:
    txt = ""
    for m in mi:
        if m == 0:
            txt += "."
        else:
            txt += "#"
    print(txt)
