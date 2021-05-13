# 盤面座標は8000x8000(x 2)
N = 8000
s = input()
target_x, target_y = map(int, input().split())

# "FTTFF" -> [1, 0, 2]と変換。'F1TF0TF2T'のFだけとる
dat_f = [len(Fcount) for Fcount in s.split("T")]

# マイナスを含むxとyのDP用配列(=x2)を作る +1するのは原点用
# x, yの閾値判定するのが面倒なので倍(=x2)用意する(index error対策)
curmap_x = [False] * ((N * 2 * 2) + 1)
curmap_y = [False] * ((N * 2 * 2) + 1)
nextmap_x = [False] * ((N * 2 * 2) + 1)
nextmap_y = [False] * ((N * 2 * 2) + 1)

# 初期座標 0,0なのだが、最初Fから始まる場合は(x,0)から始まるし、y軸を向きながら処理する
if s[0] == "F":
    start = 1
    curmap_x[N * 2 + dat_f[0]] = True
    direction_x = False
else:
    start = 0
    curmap_x[N * 2] = True
    direction_x = True

# y=0
curmap_y[N * 2] = True

# 処理すべき最初のFから
for i in range(start, len(dat_f)):
    step = dat_f[i]
    if direction_x:
        for j in range(N, N + (N * 2) + 1):
            nextmap_x[j] = True if curmap_x[j - step] or curmap_x[j + step] else False
        curmap_x, nextmap_x = nextmap_x, curmap_x
    else:
        for j in range(N, N + (N * 2) + 1):
            nextmap_y[j] = True if curmap_y[j - step] or curmap_y[j + step] else False
        curmap_y, nextmap_y = nextmap_y, curmap_y

    # くる
    direction_x = not direction_x

print("Yes" if curmap_x[N * 2 + target_x] and curmap_y[N * 2 + target_y] else "No")
