NK = list(map(int, input().split(' ')))
N = NK[0]
K = NK[1]
A = list(map(int, input().split(' ')))

for i in range(K, N):
    if (A[i-K] < A[i]):
        print('Yes')
    else:
        print('No')
