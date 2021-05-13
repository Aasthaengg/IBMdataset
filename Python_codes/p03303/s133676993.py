from math import ceil
s = list(input())
w = int(input())
for i in range(ceil(len(s)/w)):
    print(s[i*w],end="")