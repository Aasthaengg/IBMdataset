# 138a https://atcoder.jp/contests/abc138/tasks/abc138_a

# 入力
a = int(input())
s = input()

# 処理
if a < 2800 or a >= 5000:
    answer = '制約値外です'
elif a >= 3200:
    answer = s
elif a < 3200:
    answer ='red'

# 出力
print(answer)