#!/usr/bin/env python

H, W, A, B = list(map(int,input().split()))

# 1 1 1 1 1 1 0 0 0 
# 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 1 1 1
# 0 0 0 0 0 0 1 1 1
# 0 0 0 0 0 0 1 1 1


row1 = "1" * max(A, W-A) + "0" * min(A,W-A)
row2 = "0" * max(A, W-A) + "1" * min(A,W-A)
for i in range(max(B,H-B)):
    print(row1)
for i in range(min(B,H-B)):
    print(row2)