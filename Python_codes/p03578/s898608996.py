import bisect
n = int(input())
d_li = list(map(int,input().split()))
m = int(input())
t_li = list(map(int,input().split()))

import collections
d_cnt = collections.Counter(d_li)
t_cnt = collections.Counter(t_li)
#print(d_cnt,t_cnt)

for t in t_cnt.items():
    #print(d_cnt,d_cnt[t[0]],t[1])
    if d_cnt[t[0]] < t[1]:
        print('NO')
        exit()
print('YES')