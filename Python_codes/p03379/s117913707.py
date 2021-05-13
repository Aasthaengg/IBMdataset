from statistics import median
from operator import itemgetter
N = int(input())
x = list(map(int, input().split()))
x_ = sorted(x)
m0 = median(x_[1:])
m1 = median(x_[:-1])
for i in x:
    if m1 >= i:
        print(m0)
    else:
        print(m1)
    
