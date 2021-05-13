# N 人
# 身長 K cm以上必要
# i番目の身長 hi
# 乗れる人数
N, K = map(int, input().split())
h = list(map(int, input().split()))

cnt = 0
for hi in h:
    if hi >= K:
        cnt += 1
print(cnt)
