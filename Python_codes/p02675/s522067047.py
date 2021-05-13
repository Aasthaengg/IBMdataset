#!usr/bin/python3

x = int(input()) 

A = [2, 4, 5, 7, 9]
B = [0, 1, 6, 8]
C = [3]

c = int(x%10)

if c in A:
    print('hon')
if c in B:
    print("pon")
if c in C:
    print("bon")
    
