#!/mnt/c/Users/moiki/bash/env/bin/python
N,A,B = list(map(int, input().split()))


# max
print( min(N, min(A,B))  , end = " ")
# min 
print( max(0, (A+B-N) ) )
