def main():
    N, K = map(int, input().split())
    SUSHI = []
    for _ in range(N):
        t, d = map(int, input().split())
        SUSHI.append((d, t))
    SUSHI.sort(reverse=True)

    NEW = {i: True for i in range(1, N+1)} ## NEW[i]:=i番目のすしの種類がカウントされたかどうか
    x, y = 0, 0 # xは基礎ポイント、yは種類数,y*yで種類ぽいんと
    A, B = [], [] # Ａはおいしさ順に先頭K個とったときに、新種じゃないもののおいしさ
                  #　Bはおいしさ順にみたときに、Ａ以降のネタでＡに出現しなかったネタの美味しさ

    ## 以下、ＳＵＳＨＩを先頭からみて初期値x, y, A, Bを作成する
    for d, t in SUSHI[:K]:
        if NEW[t]: # 新種のネタ
            x += d
            y += 1 # 種類が増える
            NEW[t] = False
        else:
            x += d
            A.append(d)
    for d, t in SUSHI[K:]:
        if NEW[t]:
            B.append(d)
            NEW[t] = False
    B.sort()
    ### この時点で
    ### Aには先頭K種類のすしで種類ポイントに寄与しないネタ(の美味しさ)が大きい順に入っている。pop()で一番小さい値をとってこれる
    ### Bには先頭K以降のすしで種類ポイントに寄与するネタ(の美味しさ)が小さい順に入っている。pop()で一番大きい値をとってこれる。

    answer = x + y**2
    while A and B: # AかＢが空になるまで続ける
        a, b = A.pop(), B.pop() # A中種類ポイントに寄与せず、一番おいしくないネタとB中種類ポイントに寄与して、一番おいしいネタを交換
        x -= a
        x += b
        y += 1
        if x + y**2 > answer:
            answer = x + y**2
    print(answer)
main()