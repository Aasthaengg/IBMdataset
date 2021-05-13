# 同じカードが3枚以上ある場合は2枚ずつ減らせる
# 3枚以上で奇数の場合->1枚残る
# 3枚以上で偶数の場合->2枚残る

# 同じカードが2枚の場合
# 2枚のペアが２つ存在する場合
# 片方のペアから2枚選べば、両方の数字を1にできる
# ペアの数を2で割った数（切り捨て）*2のカードを減らせる

# 2枚のペアが1つ残ったとき
# そのときの全体数-2が答え

# 2枚のペアが残ってなければそのまま答え

N=int(input())
A=sorted(list(map(int,input().split())))
card=N
pairs=0
import itertools
for key,g in itertools.groupby(A):
  num=len(list(g))
  if num>2:
    if num&1:
      card-=(num-1)
    else:
      card-=(num-2)
      pairs+=1
  elif num==2:
    pairs+=1
if pairs>1:
  card-=(pairs//2)*2

if pairs&1:
  card-=2
  
print(card)