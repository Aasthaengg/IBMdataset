# coding: utf-8
# Your code here!
r,D,x2000 = map(int,input().split())

x_cur = x2000
for i in range(2001,2011):
    x_cur = r*x_cur-D
    print(x_cur)