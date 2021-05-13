import bisect

a, b, q = map(int, input().split())
ans = 0

shrine = []
temple = []

for i in range(a):
    s = int(input())
    shrine.append(s)

for i in range(b):
    t = int(input())
    temple.append(t)


for j in range(q):
    shrine_list = []
    temple_list = []
    query = int(input())
    shrine_index = bisect.bisect_left(shrine, query)
    temple_index = bisect.bisect_left(temple, query)
    if shrine_index == 0:
        shrine_list.append(shrine[shrine_index])
    elif shrine_index == len(shrine):
        shrine_list.append(shrine[shrine_index-1])
    else:
        shrine_list.append(shrine[shrine_index])
        shrine_list.append(shrine[shrine_index-1])
    if temple_index == 0:
        temple_list.append(temple[temple_index])
    elif temple_index == len(temple):
        temple_list.append(temple[temple_index-1])
    else:
        temple_list.append(temple[temple_index])
        temple_list.append(temple[temple_index-1])
    min_dist = 10**12
    for sh in shrine_list:
        for tm in temple_list:
            if sh < query < tm:
                dist = min(tm - sh + (query - sh), tm - sh + (tm - query))
            elif tm < query < sh:
                dist = min(sh - tm + (query - tm), sh - tm + (sh - query))
            elif min(query, sh, tm) == query:
                dist = max(sh, tm) - query
            elif max(query, sh, tm) == query:
                dist = query - min(sh, tm)
            if dist < min_dist:
                min_dist = dist
    print(min_dist)

