n = int(input())
a = list(map(int, input().split()))

k = 0
if max(a) == min(a):
    print(0)
    exit()
elif max(a) * min(a) < 0:
    print((n - 1) * 2)
    if max(a) + min(a) >= 0:
        k = a.index(max(a)) + 1
    else:
        k = a.index(min(a)) + 1
    for i in range(1, n + 1):
        if i != k:
            print(k, i)
else:
    print(n - 1)
    if max(a) > 0:
        k = a.index(max(a)) + 1
    else:
        k = a.index(min(a)) + 1

if a[k - 1] > 0:
    for i in range(1, n):
        print(i, i + 1)
else:
    for i in range(n, 1, -1):
        print(i, i - 1)



