# -*- coding: utf-8 -*-
# 整数の入力
# a = int(input())
# スペース区切りの整数の入力
# b, c = map(int, input().split())
# 文字列の入力
# s = input()
# 出力
# print("{} {}".format(a+b+c, s))
n,m = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in a:
    if (i >= sum(a)/(4*m)):
        cnt += 1
if (cnt >= m):
    print("Yes")
else:
    print("No")