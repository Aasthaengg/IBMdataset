# coding: utf-8
in_str = input()
a, b = in_str.split(" ")
a = int(a)
b = int(b)

if a*b % 2 == 0:
    print("Even")
else:
    print("Odd")