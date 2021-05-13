n = int(input())
a = list(map(int, input().split()))

x = [0] * n
x[0] = sum(a) - sum([a[i] for i in range(1, n, 2)]) * 2
for i in range(n-1):
    x[i+1] = 2 * a[i] - x[i]

print(' '.join(map(str, x)))
