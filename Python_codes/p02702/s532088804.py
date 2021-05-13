# -*- coding: utf-8 -*-
import math
S = input()[::-1]
remainder = [0] * 2019

# 2つ選ぶ組み合わせにおいて余り0の場合は1つしか選ばなくて良いので
# 2つ目に0を選んだ場合として便宜的に設定
remainder[0] = 1

num = 0
d = 1
for s in S:
  num += int(s) * d
  remainder[num % 2019] += 1
  d *= 10
  
  # numが大きくなりすぎると計算量が膨大になってしまうのを防ぐ
  # num%2019を計算するので、先に%2019で計算しても結果は変わらない
  d %= 2019
ans = 0
for i in range(2019):
  ans += remainder[i] * (remainder[i]-1) // 2
print(ans)