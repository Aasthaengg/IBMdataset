from collections import Counter
N = int(input())
a = Counter(list(map(int, input().split())))
b = set(a.values())
if a[0] == N:
    print('Yes')
elif N % 3 == 0:
    if len(b) == 1:
        c = [x for x in a.keys()]
        if len(c) == 3:
            if c[0] ^ c[1] ^ c[2] == 0:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif len(b) == 2:
        if a[0] == N // 3:
            if (N*2) // 3 in b:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')