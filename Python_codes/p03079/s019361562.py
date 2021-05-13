# coding: utf-8
# Your code here!
def pin(type=int):
    return map(type,input().split())


A =list(pin())
A.sort()
if (A[0] == A[1] and A[1]== A[2] ):
    print("Yes")
else:
    print("No")