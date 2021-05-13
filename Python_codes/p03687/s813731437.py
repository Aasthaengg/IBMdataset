# https://atcoder.jp/contests/agc016/tasks/agc016_a
# 真ん中らへんの文字を採用すれば結構早く同じ文字になる
# 最終的にどの文字にしたいかターゲットを絞って、操作するのを繰り返せば？(100*100*答え回の探索ですむ)
from collections import Counter
S = input()
cnt = Counter(S)
ans = 10**5
for k in cnt:
    # cnt_k = cnt[k]  # 個数管理用
    ans_k = 0
    T = list(S)
    # print(cnt_k)
    while not all([t == k for t in T]):
        ans_k += 1
        new_T = []
        for i in range(len(T) - 1):
            if T[i] == k:
                new_T.append(k)
            elif T[i + 1] == k:
                new_T.append(k)
            else:
                new_T.append(T[i])
        T = new_T
    # print(T, cnt_k)
    ans = min(ans, ans_k)
print(ans)
