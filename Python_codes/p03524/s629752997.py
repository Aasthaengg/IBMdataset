def count(l):
    res = {'a':0, 'b':0, 'c':0}
    for d in l:
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return res

string = input()
cnt = count(string).values()
if max(cnt) - min(cnt) < 2:
    print('YES')
else:
    print('NO')

