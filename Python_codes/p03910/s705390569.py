from sys import stdin
import sys
import itertools
import math

N = int(input())
if N == 1 or N == 2:
    print(N)
    sys.exit()
ans = 0
temp = []
if N > 1000:
    x = 2*int(math.sqrt(2*N))
    # print(x)
    y=[i for i in range(1,x)]
    # print(sum(y))
else:
    x = N
for i in range(1, x):
    ans += i
    temp.append(i)
    if ans >= N:
        f = ans-N
        # print("f=", f)
        for k in range(len(temp)):
            if temp[-1] <= f:
                f = f-temp[-1]
                temp.pop()
                continue
            print(temp[-1])
            temp.pop()
            # print(ans, i)
