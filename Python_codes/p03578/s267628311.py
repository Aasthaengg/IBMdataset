N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

import collections
dict_D = dict(collections.Counter(D))
dict_T = dict(collections.Counter(T))

for k, v in dict_T.items():
    if v <= dict_D.get(k, 0):
        pass
    else:
        print('NO')
        break
else:
    print('YES')
