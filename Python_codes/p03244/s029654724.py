n = int(input())
v = list(map(int, input().split()))
from collections import Counter
cnt = Counter(v)
ocnt = sorted(Counter(v[::2]).items(), key=lambda x: x[1], reverse=True)
ecnt = sorted(Counter(v[1::2]).items(), key=lambda x: x[1], reverse=True)
if len(cnt) == 1:
    print(n//2)
elif len(ocnt) == 1 and len(ecnt) == 1:
    print(0)
else:
    onum = ocnt[0][1]
    enum = ecnt[0][1]
    if ocnt[0][0] != ecnt[0][0]:
        print(n - onum - enum)
    else:
        if len(ocnt) > 1 and len(ecnt) > 1 and ocnt[1][0] != ecnt[1][0]:
            print(min(n - onum - ecnt[1][1], n - enum - ocnt[1][1], n - ecnt[1][1] - ocnt[1][1]))
        else:
            print(min(n - onum - ecnt[1][1], n - enum - ocnt[1][1]))
