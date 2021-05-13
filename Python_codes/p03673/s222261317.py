from collections import deque
n = int(input())
L = list(map(int, input().split()))
d = deque()

# 偶数奇数で最終的な向きを決める
for i in range(n):
    if (i < 2):
        d.append(str(L[i]))
    else:
        if (i % 2 == 0):
            d.appendleft(str(L[i]))
        else:
            d.append(str(L[i]))

if (len(d) % 2 == 0):
    d.reverse()
    print(' '.join(d))
else:
    print(' '.join(d))
