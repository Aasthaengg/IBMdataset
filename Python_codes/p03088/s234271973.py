# 解説AC
n = int(input())
mod = 10**9+7

# -----------DP解法----------
# ---考え方---
# 文字列として入ってはいけないものは、以下の5通り
# 'AGC', 'ACG', 'GAC', 'A?GC', 'AG?C'
# i文字目の決定に関与するのは、i-1, i-2, i-3文字目のみ

# 参考: https://drken1215.hatenablog.com/entry/2019/04/23/120400
# DP[i][i-3文字目:x][i-2文字目:y][i-1文字目:z] = 条件を満たす長さiの文字列の総数
# 以下、i文字目をmで表す

# 文字管理として、初期値:0, A:1, G:2, C:3, T:4とする
# (xyzm)として、(?123), (?132), (?213), (1?23), (12?3)が条件を満たさないパターン
# 


DP = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(n+1)] 
DP[0][0][0][0] = 1

for i in range(n):
    # i-3~i-1文字目
    for x in range(5):
        for y in range(5):
            for z in range(5):
                # i文字目
                for m in range(1,5):
                    if y == 1 and z == 2 and m == 3:
                        continue
                    elif y == 1 and z == 3 and m == 2:
                        continue
                    elif y == 2 and z == 1 and m == 3:
                        continue
                    elif x == 1 and z == 2 and m == 3:
                        continue
                    elif x == 1 and y == 2 and m == 3:
                        continue
                    DP[i+1][y][z][m] = (DP[i+1][y][z][m] + DP[i][x][y][z]) % mod

ans = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            ans = (ans + DP[n][x][y][z]) % mod

print(ans)
                    

# -----------以下はメモ化再帰解法------------

# # 先に上記文字列が入っているかどうかを判定する関数を用意する
# # 入力されるsは4文字とする
# def moji_check(s):
#     if s.count('AGC') >= 1 or s.count('ACG') >= 1 or s.count('GAC') >= 1:
#         return False
#     elif s[0] == 'A' and s[2:4] == 'GC':
#         return False
#     elif s[:2] == 'AG' and s[3] == 'C':
#         return False
#     else:
#         return True

# # メモ化再帰で求める
# # memo[i]: 現在の文字数目に登場した
# memo = [{} for i in range(n+1)]

# def dfs(cur, s):
#     if s in memo[cur]:
#         return memo[cur][s]
#     if cur == n:
#         return 1
#     ret = 0
#     for c in 'AGCT':
#         if moji_check(s+c) == True:
#             ret = (ret + dfs(cur+1, s[1:] + c)) % mod
#     memo[cur][s] = ret
#     return ret
# print(dfs(0, 'TTT'))
