import sys

N, X, M = map(int, input().split())

if N == 1: #例外
  print(X)
  sys.exit()

ans = 0
ans += X - (X%M) #XがMより大きい場合、超過分を先に計上する。
X %= M #これで 0 <= X <= M-1 が成り立つようにできた。

def fun(x): #問題の関数を用意（いちいち中身を書いていると面倒くさいため）
  return (x * x) % M

appear_set = {X} #すでに現れた数を格納する


i_0 = 1 #今までに調べた個数。現在は「X」の1つだけ。
x = X #このxに何度も関数funを作用させる
sum_0 = x #現在までの和

# ①：すでに出現したことのある数が現れるまで、ループを回す。
#  　この途中で目標回数Nに到達するなら、その時点で答えを出力する(31-33行目)。
while fun(x) not in appear_set: #次のxが初めて現れる数なら続ける。
  x = fun(x) #xにfunを作用
  appear_set.add(x) #xを「現れたものリスト」に格納
  sum_0 += x #和の更新
  i_0 += 1   #調べた個数の更新
  
  if i_0 == N: #目標回数に到達したら、その時点で答えを出力して終了。
    print(ans + sum_0)
    sys.exit()

# 現在、xには系列に初めて現れた最後の数が入っている。
# 次の数であるfun(x)は、前に現れたことのある数。したがって、ここからループが始まる。
# 整理のため、ここまでの和を計上し、残り回数も減らしておく。
ans += sum_0
N -= i_0

# ②：ループの性質を調べるため、もう一度ループを回したい。
#　欲しいものは3つ。
#   1.ループ１週の和
#   2.ループの途中までの和を記録した配列。
#   3.ループの長さ

#　以下、先ほどと異なる部分を中心に説明する。
x = fun(x) # 次の数へ行く(ループの最初の数)
appear_set_2 = {x} 
sum_1 = x        # 欲しいもの1。ループ１周の和を記録する。
sum_list = [0,x] # 欲しいもの2。i番目の要素がi番目までの数までの和を示すよう、この後要素を追加する。
i_1 = 1 # すでに調べた個数をカウントする。現在は「x」の1個だけ。
# このi_1が、最終的にループの長さ(欲しいもの3)になる。

# 以下、60行目以外の処理は先ほどと同様。
while fun(x) not in appear_set_2:
  x = fun(x)
  appear_set_2.add(x)
  sum_1 += x 
  sum_list.append(sum_1) #途中までの和を記録。
  i_1 += 1
  
# ③：上で求めた３つの情報（一周の和sum_1, 途中までの和の記録sum_list, ループ長i_1）
#    を使って答えを求める。
ans += sum_1 * (N // i_1) + sum_list[(N % i_1)]

print(ans)