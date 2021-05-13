n = int(input())
a = list(map(int, input().split()))
l = [0] *n
for i in range(n):
    tmp = a[i] if i % 2 == 0 else -a[i]
    l[0] += tmp
for i in range(n):
    if i < n-1:
        l[i + 1] = 2 * a[i] - l[i]
    else:
        l[i] = 2*a[i] -l[0]
for i in range(n):
    print(l[i], end = " ")