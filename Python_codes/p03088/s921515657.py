mod = 10**9+7
N = int(input())

A, G, C, T = 0, 1, 2, 3  # 文字を数字に割り当てる
# dp[n][最後の前の前の文字][最後の前の文字][最後の文字]:= 長さnも字列が何通り作れるか
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
# 禁止されている文字列は [AGC, GAC, ACG] と [A*GC, AG*C]
# 数字に対応させると[012, 102, 021] と [0*12, 01*2]
# 末尾の3文字 + 今見ている1文字の合計4文字だけを見ればよい
# 文頭のTが影響を与えることはないので初期化時にTを使ってもよい
dp[0][T][T][T] = 1
for n in range(N):
    for c0 in range(4):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    # 禁止のパターンならcontinue
                    if c1 == A and c2 == G and c3 == C: continue
                    if c1 == G and c2 == A and c3 == C: continue
                    if c1 == A and c2 == C and c3 == G: continue
                    if c0 == A and c1 == G and c3 == C: continue
                    if c0 == A and c2 == G and c3 == C: continue
                    # nの値を進めるとともに、末尾の3文字列
                    dp[n+1][c1][c2][c3] += dp[n][c0][c1][c2]
                    dp[n+1][c1][c2][c3] %= mod
ans = 0
for c0 in range(4):
    for c1 in range(4):
        for c2 in range(4):
            ans += dp[N][c0][c1][c2]
            ans %= mod
print(ans)
