# 参考：https://atcoder.jp/contests/abc060/submissions/3379570
# Nが高々100までなのでそれぞれ25個ずつある場合が一番場合の数が多いが25**4は10**5オーダーに収まるので問題ない

N, W = map(int, input().split())
# 物を格納
L = [list(map(int, input().split())) for _ in range(N)]

# 一つ目の物の重さが一番小さいので
w_min = L[0][0]

# 4種類の重さについて、価値を格納する
M = [[], [], [], []]
for w, v in L:
      M[w - w_min].append(v)

# それぞれについて価値の高い順に並べる
M0 = sorted(M[0], reverse=True)
M1 = sorted(M[1], reverse=True)
M2 = sorted(M[2], reverse=True)
M3 = sorted(M[3], reverse=True)

ans = 0
# それぞれをp,q,r,s個ずつ鞄に入れる時を考える
for p in range(len(M0)+1):
      for q in range(len(M1)+1):
            for r in range(len(M2)+1):
                  for s in range(len(M3)+1):
                        # 重さが制限を超えないならそれまでの最大価値と比較
                        w = p*(w_min) + q*(w_min+1) + r*(w_min+2) + s*(w_min+3)
                        if w <= W:
                              ans = max(ans, sum(M0[:p])+sum(M1[:q])+sum(M2[:r])+sum(M3[:s]))

print(ans)