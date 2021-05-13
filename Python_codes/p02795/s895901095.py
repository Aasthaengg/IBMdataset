#coding:utf-8
h = int(input())
w = int(input())
n = int(input())
#切り上げ
if h >= w:
    print(-(-n//h))
else:
    print(-(-n//w))
