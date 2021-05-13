# -*- coding=utf_8 -*-

abc = list(map(int, input().split()))

a = abc[0]
b = abc[1]
c = abc[2]

if a == b:
    result = c
elif a == c:
    result = b
elif b == c:
    result = a

print(result)
