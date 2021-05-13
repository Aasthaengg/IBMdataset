from sys import stdin

S = input()
T = input()

ans  =10000
# 全探索を実施
for i in range(len(S) - len(T) + 1):
    # 不一致だった文字数
    mat = 0
    # i番目からTの長さ分の文字列が入る
    U = S[i:i + len(T)]
    for j in range(len(T)):
        # 一文字ずつアンマッチかを確認する
        if U[j] != T[j]:
            mat += 1
    # 小さいほうが入る
    ans = min(ans, mat)

print(ans)