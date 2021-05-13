import math
from statistics import mean
import math

# -*- coding: utf-8 -*-
#整数の入力を受け取る
a,b = map(int, input().split())
list1 = [a, b]

#平均値を求め、切り上げて表示する
ave = mean(list1)
print(math.ceil(ave))