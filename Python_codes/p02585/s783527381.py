"""
1. マス同士は有効グラフの一本道になっている。で、必ずどこかでループが発生している。

2. 各点から各点に移動する場合のスコアの合計とステップ数(ループ内の場合は一周以内のもの)を前処理(dfs)で求めておく。dp[i][j] => iからjまでのスコアとステップ数

3. K > N の場合、ループを通るとスコアがマイナスになるなら（dp[i][i]がマイナスになるようなiが存在するなら）、ループを一周しない方がよい。
ループを通るとスコアがプラスになるなら、

各iに対して地点iからスタートする場合というのをシミュレートすると実装が楽そう。
K <= Nの場合はi番目からスタートして、dfsでstep数がKに到達するまで進み続けて、スコアの最大値を図る。
Kが大きい場合は、dfsで道をたどっていってループを検出したら、その時点でループスコアがマイナスかプラスかを判断して、マイナスなら終了。
プラスならループスコア*(K//ループstep)を加算してできる限りKを減らす。そこからstep数がKに到達するまでdfsで道をたどっていって最大値を求める。
各スタート地点ごとにO(N)で処理可能なので、全体ではO(N^2)で処理できる
"""
N,K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = -float("INF")

for i in range(1,N+1):
    scores = [None]*(N+1)
    steps = [None]*(N+1)
    cur = i
    score = 0
    step = 0
    loopFlag = False
    while step <= K:
        if scores[cur]!=None and not loopFlag:
            loopFlag = True
            loopScore = score - scores[cur]
            loopStep = step - steps[cur]
            ans = max(ans,score)
            restLoop = (K-step)//loopStep
            if restLoop > 0:
                restLoop -= 1
            score += restLoop*loopScore
            step += restLoop*loopStep
        scores[cur] = score
        steps[cur] = step
        if step != 0:
            ans = max(ans,score)
        p = P[cur-1]
        c = C[p-1]
        cur = p
        score += c
        step += 1

print(ans)
