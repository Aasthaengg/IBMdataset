import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools

N,K = map(int,read().split())

x = (N-1)*(N-2)//2
if K > (N-1)*(N-2)//2:
    print(-1)
    exit()

rest = x-K
UV = [(x,N) for x in range(1,N)] + list(itertools.combinations(range(1,N),2))
UV = UV[:N-1+rest]

print(len(UV))
print('\n'.join('{} {}'.format(x,y) for x,y in UV))