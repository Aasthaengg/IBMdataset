#coding:utf-8

a, b = map(int, input().split())
ans = a + b

if ans < 10:
  print(ans)
else:
  print('error')