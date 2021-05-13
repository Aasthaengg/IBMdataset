#!/usr/bin/env python

S = input()

yy = int(S[0:2])
mm = int(S[2:])

yymm = False
mmyy = False

if yy > 0 and yy < 13:
    mmyy = True
if mm > 0 and mm < 13:
    yymm = True

if yymm and mmyy :
    print("AMBIGUOUS")
elif yymm and not mmyy:
    print("YYMM")
elif not yymm and mmyy:
    print("MMYY")
else:
    print("NA")
