# coding: utf-8
# Your code here!

S = input()
w = int(input())

if len(S) / w == len(S) // w:
    length = len(S) // w
else:
    length = len(S) // w + 1

for i in range(length):
    print(S[w * i], end = "")