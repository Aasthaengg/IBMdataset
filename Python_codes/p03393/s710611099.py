from sys import stdin
import sys
# import itertools
# import math

S = input()
if S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    sys.exit()
a = [chr(i) for i in range(97, 97+26)]
b = [0 for i in range(26)]
d = dict(zip(a, b))
d1 = d
for i, v in enumerate(S):
    d[v] = d.get(v, 0)+1
for i, v in enumerate(a):
    if d[v] != 1:
        print(S+v)
        sys.exit()
temp = []
temp1 = []

for i in range(25):
    temp1 = []
    temp.append(S[-1-i])
    # print(S[-1-i], S[-1-i-1])
    for k, v in enumerate(temp):
        # print("v="+v)
        # print(S[-1-i-1], ord(S[-1-i-1]), ord(v))
        if S[-1-i-1] < v:
            temp1.append(v)
    # print(temp, temp1)
    if len(temp1) > 0:
        temp1.sort()
        print(S[:-1-i-1]+temp1[0])
        sys.exit()