# -*- coding: utf-8 -*-
# 整数の入力
# スペース区切りの整数の入力
import math
a, b = map(int, input().split())

connected_num = int(str(a) + str(b))
c = int(math.sqrt(connected_num))

if connected_num == c*c:
  print("Yes")
else:
  print("No")