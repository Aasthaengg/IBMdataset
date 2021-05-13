# -*- coding: utf-8 -*-

#----------
a,b = input().rstrip().split()
#----------

if (a == "H" and b == "H") or (a == "D" and b == "D"):
    print("H")

if (a == "H" and b == "D") or (a == "D" and b == "H"):
    print("D")
