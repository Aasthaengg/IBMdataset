# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
#N, K = map(int, input().split())
# 文字列の入力
s = input()
#開業されたN個要素を受け付ける
#list = [input() for i in range(N)]

ans = 700

if s[0] == 'o':
    ans = ans+100
if s[1] == 'o':
    ans = ans+100
if s[2] == 'o':
    ans = ans+100

print(ans)
