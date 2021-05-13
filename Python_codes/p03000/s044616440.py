n,x=list(map(int,input().split()))
l=list(map(int,input().split()))
from itertools import accumulate
l=[0]+list(accumulate(l))


from bisect import bisect_right
print(bisect_right(l,x))
