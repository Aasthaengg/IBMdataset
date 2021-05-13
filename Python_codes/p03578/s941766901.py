# 計算量O(N2M)
import collections
N = int(input())

d = collections.Counter(list(map(int,input().split())))

M = int(input())
t = list(map(int,input().split()))
t_num = t.copy()
t_num = set(list(t_num))
t = collections.Counter(t)

if N < M:
    print('NO')
    exit()

for key in t_num:
    if d[key] < t[key]:
        print('NO')
        exit()
print('YES')