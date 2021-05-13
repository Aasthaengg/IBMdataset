# coding: utf-8
# Your code here!
import sys
n=int(input())
A=list(map(int,input().split()))

for i in A:
    if i % 2 ==0:
        if i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            sys.exit()
print("APPROVED")