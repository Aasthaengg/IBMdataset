# coding: utf-8
# Your code here!
# ITP1_2_A

N = input().split()

a = int(N[0])
b = int(N[1])
if a < b:
    print("a < b")
elif a == b:
    print("a == b")
else:
    print("a > b")
