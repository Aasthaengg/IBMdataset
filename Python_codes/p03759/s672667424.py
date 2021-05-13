# -*- coding: utf-8 -*-

#----------
a,b,c = list(map(int, input().rstrip().split()))
#----------
if (b-a) == (c-b):
    print("YES")
else:
    print("NO")
