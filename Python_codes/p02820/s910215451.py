"""
入力例1

5 2
8 7 6
rsrpr

このとき、r1回目から3回目に対して勝敗が
oxo
となるようにするとよさそう。
"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
ans = 0
memo = []   # 勝つ手を出したかどうかを保存しとく。
for i in range(N):
    if i >= K and T[i] == T[i - K] and memo[i - K]:
        memo.append(False)
        continue
    if T[i] == 'r':
        ans += P
    elif T[i] == 's':
        ans += R
    else:
        ans += S
    memo.append(True)
print(ans)
