n = int(input())
lis = list(map(int, input().split()))

if lis.count(0) == n:
    print('Yes')
elif n % 3 != 0:
    print('No')
elif len(set(lis)) == 2:
    if 0 in set(lis):
        if lis.count(0) == n/3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
elif len(set(lis)) == 3:
    xor = 0
    for  a in set(lis):
        if lis.count(a) == n/3:
            xor ^= a
        else:
            print('No')
            exit()
    if xor == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')