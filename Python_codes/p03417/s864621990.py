#

N, M = list(map(int,input().split()))
if N == M == 1:
    print('1')
elif N == 1 and M > 1:
    print(M - 2)
elif M == 1 and N > 1:
    print(N - 2)
else:
    print((N - 2)*(M - 2))