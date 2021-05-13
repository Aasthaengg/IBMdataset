import math

n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]

# 最小の積載量は、最も重い荷物の重さ。または、全荷物の合計をトラック台数で割った数。
minP = max(max(W), math.ceil(sum(W) / k))
# 最大の積載量は、全荷物の合計
maxP = sum(W)

while minP < maxP:
    # 重さの最小値と最大値の半分を、積載量Pと仮定
    midP = (minP + maxP) // 2

    countTrack = 1
    calc = 0
    okFlag = True

    for w in W:
        calc += w
        
        # 積載量を超過した場合
        if calc > midP:
            # 載せずに次のトラックにまわす
            calc = w
            # トラックを1台増加
            countTrack += 1

        # トラックの最大台数を超えていたら、NG
        if countTrack > k:
            okFlag = False
            break

    # トラックの最大台数内で載せきれた場合
    if okFlag:
        # 最大値を狭めて再度処理
        maxP = midP
    else:
        # 最小値を狭めて再度処理
        minP = midP + 1

print(minP)
