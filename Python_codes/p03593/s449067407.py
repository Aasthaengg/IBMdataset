h, w = map(int, input().split())
a = [input() for _ in range(h)]
dic = {}
for i in a:
    for j in range(w):
        po = i[j]
        if po in dic.keys():
            dic[po] += 1
        else: dic[po] = 1
odd = 0
mod4 = 0
for i in dic:
    if dic[i] % 2:
        odd += 1
    if dic[i] % 4:
        mod4 += 1
if h % 2 == 0 and w % 2 == 0:
    if not mod4:
        print('Yes')
    else: print('No')
elif h % 2 and w % 2:
    if odd == 1 and mod4 <= (h//2+w//2+1):
        print('Yes')
    else: print('No')
else:
    if h % 2: k = w//2
    else: k = h//2
    if odd == 0 and mod4 <= k:
        print('Yes')
    else: print('No')