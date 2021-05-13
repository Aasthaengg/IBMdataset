# -*- coding: utf-8 -*-
import sys

N = int(input().strip())
A_list = list(map(int, input().rstrip().split()))
#-----

A_list.sort()

# Check Reports(Ai) that is correct or not.
if N%2 == 0:
    i=0
    for x in range(int(N/2)):
        if A_list[i] == A_list[i+1] == 2*x + 1:
            i += 2
            continue
        else:
            #NG
            print("0")
            sys.exit()

elif N%2 == 1:
    i=0
    for x in range( int((N-1)/2) ):
        if i == 0 and A_list[i] == 0:
            i += 1
            continue
        elif A_list[i] == A_list[i+1] == 2*x:
            i += 2
            continue
        else:
            #NG
            print("0")
            sys.exit()

# Calculate Order
order = 1
for i in range(N//2):
    order = order * 2 % (10**9 + 7)

print(order)
