# 入力
x, t = map(int, input().split())

# 処理
if x > t:
    answer = x - t
else:
    answer = 0

# 出力
print(answer)