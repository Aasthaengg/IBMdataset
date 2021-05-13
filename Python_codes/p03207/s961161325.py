# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
#N, K = map(int, input().split())
# 文字列の入力
N = int(input())
#開業されたN個要素を受け付ける
list = [int(input()) for i in range(N)]

list=sorted(list)
list.reverse()
#print(list)

ans = 0

for i, l in enumerate(list):
    if i==0:
        ans = l/2
    else:
        ans = ans + l

print(int(ans))
