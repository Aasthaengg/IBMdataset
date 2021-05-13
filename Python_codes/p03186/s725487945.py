# coding:utf-8
a,b,c = map(int, input().split())
c_eatable = c if a+b+1>c else a+b+1
print("{}".format(b+c_eatable))