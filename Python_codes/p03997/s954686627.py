#上底の長さ
a = input()
#下底の長さ
b = input()
#高さ
h = input()
#答え
ans = 0
#文字列を数値化しつつ
#(上底+下低)*高さ/2で台形の面積を求める
ans = (int(a) + int(b)) * int(h) / 2
#答えを出力
#小数点以下が表示されるのでround()で非表示にしている
print(round(ans))