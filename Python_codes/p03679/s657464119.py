# -*- coding: utf-8 -*-


#----------
X,A,B = list(map(int, input().rstrip().split()))
#----------
d=-A+B
print( "delicious" if d <= 0 else "safe" if d <= X else "dangerous")

