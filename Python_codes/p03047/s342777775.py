#https://atcoder.jp/contests/diverta2019/tasks/diverta2019_a
# -*- coding: utf-8 -*-

n,k = map(int,input().split())

answer = n-k+1
if n < k :
        answer = 0
print( answer )