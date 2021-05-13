# -*- coding: utf-8 -*-

#----------
A,B = list(map(int, input().rstrip().split()))
#----------
sum = A+B

if sum >= 10:
    print("error")
else:
    print(sum)
