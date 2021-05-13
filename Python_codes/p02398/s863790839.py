#coding:utf-8

a, b, c = map(int, raw_input(). split())
L = []
for i in xrange(a, b + 1):
    L.append(i)
y = 0
div = 0
for n in L:
    x = c % L[y]
    y += 1
    if x == 0:
        div += 1

print(div) 