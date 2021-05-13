import collections

n = int(input())
d = [int(_) for _ in input().split()]
m = int(input())
t = [int(_) for _ in input().split()]

D = collections.Counter(d)
nd = dict.fromkeys(D, 0)

for i in range(m):
    if t[i] in nd:
        get_cnt = nd[t[i]] + 1
        if get_cnt <= D[t[i]]:
            nd[t[i]] = get_cnt
        else:
            print('NO')
            exit()
    else:
        print('NO')
        exit()
print('YES')