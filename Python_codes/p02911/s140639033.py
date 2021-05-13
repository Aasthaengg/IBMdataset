import collections

N, K, Q = map(int, input().split())
A = [int(input()) - 1 for i in range(Q)]
A_count = collections.Counter(A)
A_sum = sum(A_count.values())
for i in range(N):
    if K - (A_sum - A_count[i]) <= 0:
        print('No')
    else:
        print('Yes')
