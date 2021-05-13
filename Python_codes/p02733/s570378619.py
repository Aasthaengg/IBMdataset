h, w, k = map(int, input().split())
C = [list(input()) for _ in range(h)]
# C[hCX][w]
ans = 10 ** 20
for s in range(2 ** (h - 1)):
    yoko = bin(s).count("1")
    white = [0] * (yoko + 2)
    cnt = 0
    # 横分割を足しておく
    cnt += yoko
    outflag = 0
    for j in range(w):
        now = 0
        for i in range(h):
            if outflag:
                break
            white[now] += int(C[i][j])
            if white[now] > k:
                # 縦分割をする時はkを超えた時。
                # kを超えたら1つ前で割ったことにするので、
                # その列をもう1回やり直す必要あり
                cnt += 1
                # 同じjのところをi=[0,i]までやり直す
                # 初期化
                white = [0] * (yoko + 2)
                now = 0
                # 0からiまでやり直す
                for t in range(i + 1):
                    white[now] += int(C[t][j])
                    if white[now] > k:
                        outflag = 1
                        break
                    if (s >> t) & 1 == 1:
                        now += 1
                continue
            if (s >> i) & 1 == 1:
                now += 1
        if outflag:
            break
    if outflag:
        outflag = 0
        continue
    ans = min(cnt, ans)
print(ans)
