from collections import Counter

H, W = map(int, input().split())
lis = []
for i in range(H):
    a = list(input())
    lis += a

lis = list(Counter(lis).values())
length = len(lis)

check_4 = 0
check_2 = 0
check_kisu = 0
for i in lis:
    if i % 4 == 0:
        check_4 += 1
    elif i % 2 == 0:
        check_2 += 1
    else:
        if check_kisu:
            print('No')
            exit()
        else:
            check_kisu = i % 4

if (H % 2 == 0) & (W % 2 == 0):
    if (check_kisu != 0) | (check_2 != 0):
        print('No')
        exit()

elif (H % 2 == 1) & (W % 2 == 1):
    if (H + W - 1 < check_kisu + 2 * check_2) | ((H + W - 1 - check_kisu - 2 * check_2) % 4 != 0):
        print('No')
        exit()

elif H % 2 == 1:
    if (W < 2 * check_2) | ((W - 2 * check_2) % 4 != 0):
        print('No')
        exit()


elif W % 2 == 1:
    if (H < 2 * check_2) | ((H - 2 * check_2) % 4 != 0):
        print('No')
        exit()

print('Yes')
