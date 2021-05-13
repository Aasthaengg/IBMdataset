# -*- coding:utf-8 -*-
a,b = map(int,input().split())

if  b==1:
    print(0)
elif a >= b:
    print(1)
else:
    SumPowerSocket = a
    NumUsePowerTap = 1
    while True:
        if b > SumPowerSocket:
            SumPowerSocket += a - 1
            NumUsePowerTap += 1
        else:
            print(NumUsePowerTap)
            break