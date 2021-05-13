N,M,X = map(int,input().split())
A = list(map(int,input().split()))
from bisect import bisect
i = bisect(A,X)
print(min(i,M-i))