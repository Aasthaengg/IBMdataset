#   AtCoder abc050 a
#   ストレッチ課題

#   入力
a, op, b = map(str, input().split())

#   処理
if op == "+":
    answer = int(a) + int(b)
else:
    answer = int(a) - int(b)

#   出力
print(answer)

