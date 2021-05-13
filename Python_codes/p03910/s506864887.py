from itertools import accumulate
import bisect
n=int(input())
l=list(accumulate(range(4473)))
while True:
    i=bisect.bisect_left(l,n)
    if i<1:break
    print(i)
    n-=i