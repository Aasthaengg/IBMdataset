n, k, q = list(map(int, input().split()))

# 回答者毎の正解数を0で初期化
ns_corrects = [0] * n

for i in range(q):
    # 回答者毎の正解数をカウント
    ns_corrects[int(input())-1] += 1


for j in range(n):
    # 回答者毎に「問題数―正解数=減点数」をカウントし持ち点が無くなれば'No'
    if k - (q - ns_corrects[j]) <= 0:
        print('No')
    else:
        print('Yes')