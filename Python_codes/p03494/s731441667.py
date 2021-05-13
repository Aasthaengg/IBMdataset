# -*- coding: utf-8 -*-
# 整数の入力
size = int(input())
nums = [int(s) for s in input().split()]

count = 0
checked = False

while True:
  for i in range(size):
    t = nums[i]
    if t % 2 == 1:
      checked = True
      break;
    nums[i] = t/2
  if checked:
    break
  count = count + 1

print(count)
