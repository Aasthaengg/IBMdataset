S = list(input())
N = len(S)

# n文字まで見て最後が1文字か2文字化
dp_1 = [0] * N
dp_2 = [0] * N
dp_1[0] = 1
dp_2[1] = 1
if S[0] != S[1]:
    dp_1[1] = 2


for i, s in enumerate(S[2:], 2):
    # dp_1
    # 2 -> 1
    tmp = dp_2[i - 1] + 1
    # 1 -> 1
    if S[i - 1] != S[i]:
        tmp = max(tmp, dp_1[i - 1] + 1)
    dp_1[i] = tmp

    # dp_2
    # 1->2
    tmp = dp_1[i - 2] + 1
    # 2->2
    if S[i - 3 : i - 1] != S[i - 1 : i + 1]:
        tmp = max(tmp, dp_2[i - 2] + 1)
    dp_2[i] = tmp

print(max(dp_1[-1], dp_2[-1]))
