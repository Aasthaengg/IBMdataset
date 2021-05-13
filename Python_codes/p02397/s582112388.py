#coding:utf-8

wh = 1
wh2 = 2
L = []
while wh < wh2:
    x, y = map(int, raw_input(). split())
    if x == 0 and y == 0:
        break
    else:
        L.append(x)
        L.append(y)


i = 0
while i < len(L):
    a = L[i]
    b = L[i + 1]
    if a < b:
        print(str(a) + " " + str(b))
    else:
        print(str(b) + " " + str(a))
    i += 2