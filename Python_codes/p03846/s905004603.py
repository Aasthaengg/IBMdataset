n = int(input())
a = list(map(int, input().split()))
a.sort()
if n % 2 == 1:
    if a[0] != 0:
        print(0)
    else:
        for i in range(2, n, 2):
            if not i == a[i-1] == a[i]:
                print(0)
                break
        else: print((2**(n//2))%1000000007)
else:
    for i in range(1, n, 2):
        if not i == a[i-1] == a[i]:
            print(0)
            break
    else: print((2**(n//2))%1000000007)