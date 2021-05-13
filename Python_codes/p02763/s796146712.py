from bisect import bisect_right
from bisect import bisect_left

n = int(input())
s = list(input())
q = int(input())

ind_list = [[] for _ in range(26)]

for i, x in enumerate(s):
    ind_list[ord(x)-97].append(i)

for _ in range(q):
    _type, val1, val2 = input().split()
    if _type == '1':
        i = int(val1)-1
        c = val2
        if s[i] == c:
            continue
        ind_list[ord(s[i])-97].remove(i)
        p = bisect_right(ind_list[ord(c)-97], i)
        ind_list[ord(c)-97].insert(p, i)
        s[i] = c
    elif _type == '2':
        l = int(val1)-1
        r = int(val2)-1
        ans = 0
        for i in range(26):
            if bisect_right(ind_list[i], r) - bisect_left(ind_list[i], l) > 0:
                ans += 1
        print(ans)
    else:
        print('Exception caught!')
        exit()
