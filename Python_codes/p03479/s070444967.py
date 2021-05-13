# -*- coding: utf-8 -*-
# import math

X,Y = list(map(int, input().rstrip().split()))
#-----

calc = X
cnt = 0

while calc <= Y:
    calc *= 2
    cnt += 1

print(cnt)


# エラーになる・・・
# calc = math.log( (Y / X) , 2) + 1
# print( int(calc) )
