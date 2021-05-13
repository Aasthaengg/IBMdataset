n, k, q = map(int,input().split())
a = dict((i,0) for i in range(1,n+1))

for _ in range(q):
    a[int(input())] += 1

for i in range(1, n + 1):
    print('Yes' if k - q + a[i] > 0 else 'No')