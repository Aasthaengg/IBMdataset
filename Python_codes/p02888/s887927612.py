n = int(input())
l = list(map(int,input().split()))

import bisect
l.sort()
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        idx = bisect.bisect_left(l,l[i]+l[j])
        #print('idx',idx)
        if j < idx:
            cnt += idx - j - 1


print(cnt)