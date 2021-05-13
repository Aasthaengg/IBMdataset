# coding: utf-8
# Your code here!
import sys
n=int(input())
for i in range(1,10):
    for j in range(1,10):
        if i*j==n:
            print("Yes")
            sys.exit()
print("No")
