n = int(input())
a = list(map(int, input().split()))

m = [0 for i in range(n)]
for i in range(n):
    if i%2 == 0:
        m[0] += a[i]
    else:
        m[0] -= a[i]
for i in range(1, n):
    m[i] = 2*a[i-1] - m[i-1]

print(' '.join(map(str, m)))