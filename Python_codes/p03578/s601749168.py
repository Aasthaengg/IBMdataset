import collections
N = int(input())
D = collections.Counter(map(int,input().split()))
M = int(input())
T = collections.Counter(list(map(int,input().split())))
for key in T.keys():
    if T[key] > D[key]:
        print('NO')
        exit()
print('YES')