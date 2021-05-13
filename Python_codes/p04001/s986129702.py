# https://atcoder.jp/contests/arc061/tasks/arc061_a
# 復習課題
# シフト演算を用いてリファクタリングせよ。

S = list(input())
ans = 0

for i in range(2**(len(S)-1)):
    p = list(bin(i))
    flag = ['0' for _ in range(len(S) - len(p) + 1)] + p[2:]
    l = 0
    for j in range(len(S)-1):
        if (i >> j) & 1:
            ans += int("".join(S[l:j+1]))
            l = j+1
    ans += int("".join(S[l:]))

print(ans)
