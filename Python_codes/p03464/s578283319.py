import math
K = int(input())
A = list(map(int,input().split()))
lo = 2
hi = 2
for e in A[::-1]:
    if hi//e == lo//e and (hi%e)*(lo%e) != 0:
        print(-1)
        exit(0)
    else:
        lo = e*math.ceil(lo/e)
        hi = e*((hi//e)+1)-1
print(lo,hi)
