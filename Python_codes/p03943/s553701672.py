#   AtCoder abc047 a
#   ストレッチ課題

#   入力
a, b, c = map(int, input().split())

#   判定
if ((a + b) == c) or ((a + c) == b) or ((b + c) == a):
    print("Yes")
else:
    print("No")
