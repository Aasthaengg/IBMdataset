N, K = map(int, input().split())
A_LIST = list(map(int, input().split()))

for index in range(K, N):
    if A_LIST[index] > A_LIST[index - K]:
        print('Yes')
    else:
        print('No')
