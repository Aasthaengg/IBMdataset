# coding: utf-8

s = input()
w = int(input())

for i,c in enumerate(s):
    if i % w == 0:
        print(c, end="")

print()
