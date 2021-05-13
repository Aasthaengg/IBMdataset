from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt_a = Counter(a)

if n % 3 == 0:
    if cnt_a[0] == n:
        print('Yes')
    elif len(set(a)) == 2 and 0 in set(a) and cnt_a[0] == n // 3:
        print('Yes')
    elif len(set(a)) == 3:
        x, y, z = set(a)
        if cnt_a[x] == n // 3 and cnt_a[y] == n // 3 and cnt_a[z] == n // 3 and x ^ y ^ z == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    if cnt_a[0] == n:
        print('Yes')
    else:
        print('No')