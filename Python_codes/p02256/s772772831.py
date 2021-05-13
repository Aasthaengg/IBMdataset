#coding:utf-8
x,y = list(map(int,input().split()))
if x < y:
    x,y = y,x
r = x % y

while r != 0:
    x = y
    y = r
    r = x % y

print(y)