N = int(input())
A = list(map(int, input().split()))

if A[-1] > 2:
    print(-1)
    exit()

"""
愚直解
初めの人数を2から増やしていって確認。範囲が分からないので、間に合わないのは分かるが計算量は分からん。

問題的にも最後から最初に戻るのがよさそう。
問題的に、Aiの処理を受けたすぐの人数をCiとする。また、ラウンドiの後にとりうる最大の人数をHIi,最小をLOiとする
考えるうえでややこしいのだが、

HIi-1                 HIi
 Ci-1   ->  {Ai} ->    Ci
LOi-1                 LOi

の形になっていて、
「LOi-1~HIi-1 の範囲の値が、  Aiの処理を受けたときに、HIiやLOiの範囲に収まらなければならない」
であるので、HIi-1,LOi-1 が Ai,HIi,LOiに依存している。
（HIi,LOiがAiで決まるのではないのに気を付けたい）

最後の状態（HIi = LOi = Ci = 2）が決まっているので、後ろから先頭に戻る形で、HIi-1, LOi-1を決めていく。

LOi-1を　Aiに通した後の値が LOi であるのは自明で、「LOi-1はAiの定数倍かつ、LOi以上」であるから
LOi-1 = (Loi // Ai) * Ai
といえる

HIi-1 を Ai に通した後に、HIi以下に収まらなければならないので、
HIi-1 = (HIi // Ai) * Ai + (Ai - 1)
となる。ここちょっと発想しにくい感じある。
(HIi // Ai + 1) * Ai が、Aiを通すと、HIiを上回るので、これより小さい物の中で最も大きいものを選びたいから。


"""


HI = 2
LO = 2
for i in range(N):
    
    if LO // A[N-i-1] > 0:
        if LO % A[N-i-1] > 0:
            nxt_LO = (LO // A[N-i-1] + 1) * A[N-i-1]
        else:
            nxt_LO = LO
    else:
        nxt_LO = A[N-i-1]

    
    
    nxt_HI = (HI // A[N-i-1]) * A[N-i-1] + (A[N-i-1] - 1)

    if HI > nxt_HI or LO > nxt_LO  or nxt_HI < nxt_LO:
        print(-1)
        exit()

    LO = nxt_LO
    HI = nxt_HI

print(LO, HI)