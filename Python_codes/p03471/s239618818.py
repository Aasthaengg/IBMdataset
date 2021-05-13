import itertools
import sys

N, Y = map(int,input().split())
rtn = False
 
for i,j in itertools.combinations_with_replacement(range(N+1), 2):
    if Y == 10000 * i + 5000 * (j-i) + 1000 * (N-j):
        print(i, j-i, N-j)
        rtn = True
        break

if not(rtn) :
    print(-1, -1, -1)