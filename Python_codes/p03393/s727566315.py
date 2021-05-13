s = input()
if len(s) != 26:
    x = sorted(set(map(chr, range(97, 123)))-set(s))
    print(s+x[0])
else:
    num = list(map(lambda x: ord(x)-ord('a'), s))
    for i in reversed(range(25)):
        L, R = i, i+1
        if num[L] < num[R]:
            tmp = 26
            for r in num[R:]:
                if num[L] < r:
                    tmp = min(tmp, r)
            ans = num[:L]+[tmp]
            print(''.join(map(lambda x: chr(x+ord('a')), ans)))
            break
    else:
        print(-1)
