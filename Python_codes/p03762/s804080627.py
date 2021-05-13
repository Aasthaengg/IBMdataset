# -*- coding: utf-8 -*-
# 整数の入力
n,m= map(int, input().split())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
yoko=0
tate=0
for i in range (0,len(x)):
  yoko+=(n-2*i-1)*x[i]
for i in range (0,len(y)):
  tate+=(m-2*i-1)*y[i]

print(yoko*tate%(10**9+7))