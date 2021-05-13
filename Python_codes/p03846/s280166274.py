n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    if a[0] == 0:
        print(1)
    else:
        print(0)
    exit()

mod = 10**9 + 7
if n % 2 == 1:
    if a[0] == 0 and a[1] == 0:
        print(0)
        exit()
    ans = 1
    for i in range(1, n, 2):
        if not(a[i] == a[i+1] and a[i] == i+1):
            print(0)
            exit()
        else:
            ans *= 2
    print(ans % mod)
else:
    ans = 1
    for i in range(0, n, 2):
        if not(a[i] == a[i+1] and a[i] == i+1):
            print(0)
            exit()
        else:
            ans *= 2
    print(ans % mod)
