n=int(input())
per=[i+1 for i in range(n)]
from itertools import permutations
per=list(permutations(per,n))

from bisect import bisect_left
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))

print(abs(bisect_left(per,p)-bisect_left(per,q)))
