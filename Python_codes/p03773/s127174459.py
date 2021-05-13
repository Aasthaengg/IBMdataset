# 入力
a, b = map(int, input().split())

total_time= a + b

# 処理&出力
if total_time >= 24:
    answer = (total_time) % 24
elif a+b < 24:
    answer = total_time

print(answer)