def count(l):
    res = {}
    for d in l:
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return res

n = float(input())
data = list(map(int, input().split()))
t = count(data)
if len(t) == 3:
    ks = list(t.keys())
    if 0 not in t and all(i == n/3 for i in t.values()) and ks[0]^ks[1] == ks[2]:
        print('Yes')
    else:
        print('No')

elif len(t) == 2:
    if 0 in t and t[0] == n/3:
        print('Yes')
    else:
        print('No')

elif len(t) == 1:
    if 0 in t:
        print('Yes')
    else:
        print('No')

else:
    print('No')
        
