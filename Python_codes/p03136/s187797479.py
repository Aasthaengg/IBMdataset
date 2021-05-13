N = int(input())
L = list(map(int, input().split()))

max_L = max(L)
sum_L = sum(L)

if max_L < sum_L - max_L:
    print('Yes')
else:
    print('No')