N, M = map(int, input().split())

INF = float("inf")
# bitで表される状態を満たすための最小コスト
# ex. N=2
# [00]=1つも開かない, [01]=1だけ開く, [10]=2だけ開く, [11]=1,2の両方開く
dp = [INF] * (2**N)
# 1つも開かない状態はコスト0で実現される
dp[0] = 0

for i in range(1, M + 1):
    a, b = map(int, input().split())

    # ex.
    # c = [1] -> tmp = 01(2) = 1
    # c = [2] -> tmp = 10(2) = 2
    # c = [1,2] -> tmp = 11(2) = 3
    tmp = 0
    for c in list(map(int, input().split())):
        tmp += 1 << (c - 1)

    # target = ある状態(j)に対して、鍵(tmp)を使った後の状態
    # ex.
    # 状態00に鍵01を使う -> 結果は01(1が新しく開く)
    # 状態01に鍵01を使う -> 結果は01（変わらない）
    # 状態10に鍵01を使う -> 結果は11（１が新しく開く）
    # 状態11に鍵01を使う -> 結果は11（１が新しく開く）
    for j in range(2**N):
        # | = 論理和(OR)
        target = j | tmp
        # 状態jから鍵のコストaを支払ってtargetに遷移 or そのまま
        dp[target] = min(dp[j] + a, dp[target])

# 更新されていない場合、全て開けることは実現できない
if dp[2**N - 1] == INF:
    print(-1)
# 更新されている場合、全て開けることが可能
else:
    print(dp[2**N - 1])
