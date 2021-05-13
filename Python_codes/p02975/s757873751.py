from collections import Counter
N = int(input())
a = list(map(int,input().split()))
if sum(a) == 0:
    print('Yes')
else:
    if len(a)%3 != 0:
        print('No')
    else:
        counter = Counter(a)
        keys = list(counter.keys())
        vlen = len(set(counter.values()))
        if len(keys) >= 4 or len(keys) == 1:
            print('No')
        else:
            if len(keys) == 2:
                if 0 in counter:
                    if counter[0] == N//3:
                        print('Yes')
                    else:
                        print('No')
                else:
                    print('No')
            else:
                if (vlen == 1) and (keys[0]^keys[1]==keys[2]):
                    print('Yes')
                else:
                    print('No')