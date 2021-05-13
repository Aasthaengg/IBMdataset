import math

N,K = (int(x) for x in input().split())
A = list(map(int, input().split()))
if N == K:
    print('1')
else:
    print(math.ceil((N-1)/(K-1)))