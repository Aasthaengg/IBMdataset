from collections import Counter, defaultdict
H, W = map(int, input().split(' '))
d = defaultdict(int)
for i in range(H):
    for k, v in Counter(input()).items():
        d[k] += v
if H % 2 == 0 and W % 2 == 0:
    for i in d.values():
        if i % 4 != 0:
            print('No')
            exit()
    print('Yes')
elif H % 2 == 0 or W % 2 == 0:
    cnt = H//2 if not H % 2 else W//2
    for i in d.values():
        if i % 4 == 0:
            continue
        elif i % 2 == 0:
            cnt -= 1
            if cnt >= 0:
                continue
        print('No')
        exit()
    print('Yes')
else:
    odd = 1
    cnt = (H+W-2)//2
    for i in d.values():
        if i % 2 != 0 and odd:
            odd -= 1
            continue
        elif i % 4 == 0:
            continue
        elif i % 2 == 0 and cnt:
            cnt -= 1
            continue
        else:
            print('No')
            exit()
    print('Yes')
