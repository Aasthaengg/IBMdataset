# -*- coding: utf-8 -*-
# 整数の入力
N = int(input())

data_list = []
for i in range(N):
  data_list.append(int(input()))

print(len(set(data_list)))