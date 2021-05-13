# 099a https://atcoder.jp/contests/abc099/tasks/abc099_a

# 入力
N = int(input()) # Nはコンテスト開催数　N回目

# 処理
if N < 1 or N > 1998:
    answer = '値が制約外です'
elif N <= 999:
    answer = 'ABC'
else:
    answer = 'ABD'

# 出力
print(answer)