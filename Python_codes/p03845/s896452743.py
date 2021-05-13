import copy
N = int(input())
T = list(map(int,input().split()))
M = int(input())

res = []
for _ in range(M):
    tmp = copy.copy(T)
    P,X = map(int,input().split())
    tmp[P-1] = X
    res.append(sum(tmp))
for i in res:
    print(i)