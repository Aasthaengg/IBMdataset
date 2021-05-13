import collections
N,K,Q = map(int,input().split())

A = [input() for i in range(Q)]

c = collections.Counter(A)

for i in range(1,N+1):

    if (Q-c[str(i)]) >=K:
        print('No')
    else:print('Yes')

