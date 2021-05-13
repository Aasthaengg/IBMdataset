N, K = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

for i in range(K, N):
    if a[i-K] < a[i]:
        print('Yes')
    else :
        print('No')
