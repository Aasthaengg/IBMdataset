from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))
if N == K:
    print(1)
elif (N-1)%(K-1) == 0:
    print((N-1)//(K-1))
elif K == 2:
    print(N-1)
else:
    ans = ceil(N/(K-1))
    print(ans)
