# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0

i = 0
for i in range(N):
  # 前日よりも株価が上がっている場合は、株を全て売却
  if i != 0 and A[i] > A[i-1]:
    money += stock * A[i]
    stock = 0
  
  # 翌日に株価が上がる場合は、所持金を全て株に変える
  if i != (N-1) and A[i+1] > A[i]:
    stock += money // A[i]
    money = money % A[i]
print(money)