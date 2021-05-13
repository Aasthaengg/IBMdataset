mod = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))

a.sort()

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            if a[i] != i + 1:
                print(0)
                exit()
        else:
            if a[i] != i:
                print(0)
                exit()
    print(pow(2, n//2, mod))

else:
    for i in range(n):
        if i % 2 == 0:
            if a[i] != i:
                print(0)
                exit()
        else:
            if a[i] != i + 1:
                print(0)
                exit()
    print(pow(2, n//2, mod))