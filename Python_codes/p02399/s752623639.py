#coding:UTF-8

a,b = map(int,raw_input().split())
d = a/b
r = a%b
f = float(a)/b
f = '%.8f' % (float(a)/b)

print d,r,f