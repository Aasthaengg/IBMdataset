

import bisect

def nearest(x, lst):
    p = bisect.bisect_left(lst, x)
    
    if p == 0:
        return lst[p], None
    if p == len(lst):
        return lst[p - 1], None
    if lst[p] == x:
        return lst[p], None
    return lst[p - 1], lst[p]
 

def submit():
    a, b, q = map(int, input().split())

    slist = [int(input()) for _ in range(a)]
    tlist = [int(input()) for _ in range(b)]
    qlist = [int(input()) for _ in range(q)]

    near_s = {s: nearest(s, tlist) for s in slist}
    near_t = {t: nearest(t, slist) for t in tlist}

    anss = []
    for q in qlist:
        ans = float('inf')
        # 一番近いs->tの順の場合
        n = nearest(q, slist)
        for e in n:
            if not e: 
                continue
            for ee in near_s[e]:
                if not ee:
                    continue
                if ans > abs(q - e) + abs(ee - e):
                    ans = abs(q - e) + abs(ee - e)                            
        # 一番近いt->sの順の場合
        n = nearest(q, tlist)
        for e in n:
            if not e:
                continue
            for ee in near_t[e]:
                if not ee:
                    continue
                if ans > abs(q - e) + abs(ee - e):
                    ans = abs(q - e) + abs(ee - e)
        anss.append(ans)

    for ans in anss:
        print(ans)


submit()

