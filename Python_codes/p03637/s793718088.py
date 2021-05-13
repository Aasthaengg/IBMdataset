N = int(input())
a = list(map(int, input().split()))
from collections import deque
kisuu = deque([])
bai4 = deque([])
sonota = deque([])
for ai in a:
    if ai % 4 == 0:
        bai4.append(ai)
    elif ai % 2 == 0:
        sonota.append(ai)
    else:
        kisuu.append(ai)

ans = deque([])
if kisuu:
    s = kisuu.pop()
    ans.append(s)
elif sonota:
    s = sonota.pop()
    ans.append(s)
else:
    s = bai4.pop()
    ans.append(s)        

for i in range(1, N + 1):
    if i == N:
        print('Yes')
        quit()
    if ans[i - 1] % 2 == 1:
        if bai4:
            s = bai4.pop()
            ans.append(s)
        else:
            break
    elif ans[i - 1] % 2 == 0 and ans[i - 1] % 4 != 0:
        if sonota:
            s = sonota.pop()
            ans.append(s)
        elif bai4:
            s = bai4.pop()
            ans.append(s)
        else:
            break
    elif ans[i - 1] % 4 == 0:
        if kisuu:
            s = kisuu.pop()
            ans.append(s)
        elif sonota:
            s = sonota.pop()
            ans.append(s)
        elif bai4:
            s = bai4.pop()
            ans.append(s)
        else:
            break
print('No')           