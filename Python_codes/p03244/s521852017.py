n = int(input())
li = list(map(int,input().split()))

ki = li[::2]
gu = li[1::2]

ki.sort()
gu.sort()

from itertools import groupby

ki_li = []
gu_li = []

for key, value in groupby(ki):
    ki_li.append((key,len(list(value))))

for key, value in groupby(gu):
    gu_li.append((key,len(list(value))))

ki_li.sort(key=lambda x:(x[1]*(-1)))
gu_li.sort(key=lambda x:(x[1]*(-1)))

if ki_li[0][0] == gu_li[0][0]:
    if ki_li[0][1] > gu_li[0][1]:
        if len(gu_li) >= 2:
            ans = n-ki_li[0][1]-gu_li[1][1]
        else:
            ans = n-ki_li[0][1]
    elif ki_li[0][1] == gu_li[0][1]:
        if len(ki_li) >= 2:
            if ki_li[1][1] >= gu_li[1][1]:
                ans = n-gu_li[0][1]-ki_li[1][1]
            else:
                ans = n-ki_li[0][1]-gu_li[1][1]
        else:
            ans = n-ki_li[0][1]
    else:
        if len(ki_li) >= 2:
            ans = n-gu_li[0][1]-ki_li[1][1]
        else:
            ans = n-gu_li[0][1]
else:
    ans = n-gu_li[0][1]-ki_li[0][1]

print(ans)