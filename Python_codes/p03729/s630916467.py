# -*- coding: utf-8 -*-

a,b,c = input().split()

lis_a = list(a)
lis_b = list(b)
lis_c = list(c)

isATrue = (lis_a[-1] == lis_b[0])
isBTrue = (lis_b[-1] == lis_c[0])

if isATrue and isBTrue:
    print("YES")
else:
    print("NO")