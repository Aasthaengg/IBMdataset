n = int(input())
a = [0] + [int(i) for i in input().split()] + [0]
d1a = [abs(a[i + 1] - a[i]) for i in range(n + 1)]
d2a = [abs(a[i + 1] - a[i - 1]) for i in range(1, n + 1)]
sum_a = sum(d1a)
for i in range(1, n + 1):
    print(sum_a + d2a[i - 1] - (d1a[i - 1] + d1a[i]))