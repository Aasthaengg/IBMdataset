import itertools, copy
h,w,k = map(int, input().split())
c = []
for i in range(h):
    cc = list(input())
    c.append(cc)
li_h = range(h)
li_w = range(w)
count = 0
for n in range(0, len(li_h)+1):
    for conb_h in itertools.combinations(li_h, n):        
        for m in range(0, len(li_w)+1):
            for conb_w in itertools.combinations(li_w, m):
                ccc = copy.deepcopy(c)
                for i in list(conb_h):
                    for ii in range(w):
                        ccc[int(i)][ii] = '.'
                for j in list(conb_w):
                    for jj in range(h):
                        ccc[jj][int(j)] = '.'
                _count = 0
                for item in ccc:
                    _count += item.count('#')
                if _count == k:
                    count += 1
print(count)