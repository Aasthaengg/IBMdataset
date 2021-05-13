# coding: utf-8

judge = input().split()

if (int(judge[0]) * int(judge[1])) % 2 == 1:
    print("Odd")
else:
    print("Even")