n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, n-k):
    if a[i] >= a[i+k]:
        print('No')
    else:
        print('Yes')