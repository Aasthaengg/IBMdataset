from collections import Counter
N = int(input())
a_ls = list(map(int, input().split()))

if N % 3 != 0:
    res = 'Yes'
    for i in range(N):
        if a_ls[i] != 0:
            res = 'No'
else:
    res = 'Yes'
    c = Counter(a_ls)
    if len(c) > 3:
        res = 'No'
    if len(c) == 3:
        if not list(c.values())[0] == list(c.values())[1] == list(c.values())[2]:
            res = 'No'
        for i in c.keys():
            for j in c.keys():
                for k in c.keys():
                    if i!=j and j!=k and k!=i and not i^j==k:
                        res = 'No'
    elif len(c) == 2:
        if not (list(c.values())[0] == N//3 or list(c.values())[1] == N//3):
            res = 'No'
        if list(c.values())[0] == N//3:
            if not list(c.keys())[0] == 0:
                res = 'No'
        if list(c.values())[1] == N//3:
            if not list(c.keys())[1] == 0:
                res = 'No'
    else:
        for i in range(N):
            if a_ls[i] != 0:
                res = 'No'
        
print(res)