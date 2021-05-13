# -*- coding: utf-8 -*-
A,B,C=map(int,input().split())
SUM=A+B+C
MAX=max(A,B,C)*3
if (MAX-SUM)%2==0:
    count=(MAX-SUM)/2
else:
    count=(MAX-SUM)/2+2
print(int(count))
