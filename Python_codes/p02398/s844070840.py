# -*- coding: utf-8 -*- 
### 数値　a b c をスペース区切りで読み込み
### c の約数がa<=b の間にいくつあるかを表示する。

#数値入力・変換
str_in = raw_input()
int_in = map(int, str_in.split())

# a〜bの約数の数を求める
counter = 0
for i in range(int_in[0], int_in[1]+1):
	if int_in[2] % i == 0:
		counter = counter + 1
		
# 個数を表示する。
print(counter)

