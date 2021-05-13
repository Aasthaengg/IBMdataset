n = int(input())
MOD = 10**9+7
a = list(map(int,input().split()))
if n == 1 and a[0] == 0:
    print(1)
    exit()
elif n == 1:
    print(0)
    exit()
if n == 2 and a[0] == 1 and a[1] == 1:
    print(1)
    exit()
elif n == 2:
    print(0)
    exit()
a.sort()
if n % 2 == 0:
    if a[0] != 1 or a[1] != 1 or a[2] == 1:
        print(0)
        exit()
    j = 3
    for i in range(2,n,2):
        if a[i] != j:
            print(0)
            exit()
        j += 2
    j = 3
    for i in range(3,n,2):
        if a[i] != j:
            print(0)
            exit()
        j+=2
if n % 2 != 0:
    if a[0] != 0 or a[1] == 0:
        print(0)
        exit()
    j = 2
    for i in range(1,n,2):
        if a[i] != j:
            print(0)
            exit()
        j += 2
    j = 2
    for i in range(2,n,2):
        if a[i] != j:
            print(0)
            exit()
        j+=2
print(pow(2,(n//2),MOD))