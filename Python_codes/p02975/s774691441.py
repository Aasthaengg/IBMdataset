from collections import Counter

n = int(input())
A = list(map(int,input().split()))

cnt = Counter(A)

if len(cnt) == 1:
    if cnt[0] == n:
        print('Yes')
    else:
        print('No')
elif len(cnt) == 2:
    if cnt[0] == n/3:
        print('Yes')
    else:
        print('No')
elif len(cnt) == 3:
    test = 0
    for p in cnt.keys():
        if cnt[p] != n/3:
            print('No')
            break
        test ^= p
    else:
        if not test:
            print('Yes')
        else:
            print('No')
else:
    print('No')