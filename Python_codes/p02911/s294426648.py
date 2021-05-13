n, k, q = map(int, input().split())
# n:参加人数
# k:初期ポイント
# q:正解の回数

# 最初のポイント初期化
menber_point = [k for _ in range(n)]

# 正解者リスト
correct_answer = [int(input()) for _ in range(q)]

# 正解したらポイント加算してあげる
for value in correct_answer:
    menber_point[value-1] += 1

# 正解の回数以下なら敗退判定
for mem in menber_point:
    if mem > q:
        print('Yes')
    else:
        print('No')