n = int(input())
a = list(map(int, input().split()))
if n % 3 == 0:
    a.sort()
    for i in range(n // 3 - 1):
        if a[i] != a[i + 1]:
            print('No')
            exit(0)
    for i in range(n // 3, n // 3 * 2 - 1):
        if a[i] != a[i + 1]:
            print('No')
            exit(0)
    for i in range(n // 3 * 2, n - 1):
        if a[i] != a[i + 1]:
            print('No')
            exit(0)
    if a[0] ^ a[n // 3] == a[n // 3 * 2]:
        print('Yes')
    else:
        print('No')
else:
    if any(a):
        print('No')
    else:
        print('Yes')
