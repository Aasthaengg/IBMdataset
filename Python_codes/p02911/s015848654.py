n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

pts = [0 for _ in range(n)]
for i in range(q):
    pts[a[i] - 1] += 1

for i in range(n):
    if k - (q - pts[i]) > 0:
        print('Yes')
    else:
        print('No')
