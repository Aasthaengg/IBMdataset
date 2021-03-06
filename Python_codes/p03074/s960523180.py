N, K = list(map(int, input().split()))
S = input()

S = S + 'E'   # 終端処理
ans = -1    # 答えの初期値（十分に小さい値）

# 立った人の連続の数
if (S[0] == '0'):
    stand = 1
else:
    stand = 0

L = 0
R = 0

# 尺取り法
while (R < N):
    # 右端を進めることが可能（立った人の連続の数がK以下）なら、右端を進める
    if (stand <= K):
        # 立った人の連続の数が増えるなら1足す
        if (S[R] == '1' and S[R + 1] == '0'):
            stand += 1
        # 答えの更新
        ans = max(ans, R - L + 1)
        R += 1
    # 進められない場合、左端と右端が同じなら両者を進める
    # 左端が右端を追い越さないための処理
    elif (L == R):
        L += 1
        R += 1
    # それ以外は左端のみを進める
    else:
        # 立った人の連続の数が減るなら1減らす
        if (S[L] == '0' and S[L + 1] == '1'):
            stand -= 1
        L += 1
        # 左端のみを進めた場合は答えを更新し得ない

print(ans)