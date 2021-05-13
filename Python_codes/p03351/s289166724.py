# -*- coding: utf-8 -*-


#----------
a,b,c,d = [int(i) for i in input().rstrip().split()]
#----------

Flag = False
if abs(c-a) <= d:
    Flag = True
elif (abs(b-a) <= d) and (abs(c-b) <= d):
    Flag = True

print("Yes" if Flag==True else "No")
