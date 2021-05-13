from sys import stdin
from math import ceil, floor
n=int(stdin.readline().rstrip())
min_ = n/1.08
max_ = (n+1)/1.08
if float(max_).is_integer():
    if ceil(min_) == floor(max_)-1:
        print(ceil(min_))
    else:
        print(":(")
else:
    if ceil(min_) == floor(max_):
        print(ceil(min_))
    else:
        print(":(")