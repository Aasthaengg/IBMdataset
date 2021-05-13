# -*- coding: utf-8 -*-


#----------
N,A,B = list(map(int, input().rstrip().split()))
#----------
num_between = abs(A-B) - 1
if (num_between % 2) == 0:
    print("Borys")
else:
    print("Alice")
