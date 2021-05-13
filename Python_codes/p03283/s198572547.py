import numpy as np

n,m,q = map(int,input().split())
li = [[0 for i in range(n+1)]for j in range(n+1)]

for i in range(m):
    l,r = map(int,input().split())
    li[l][r] += 1

li = np.array(li)
c = np.cumsum(li,axis=1).cumsum(axis=0).tolist()

for i in range(q):
    l,r = map(int,input().split())
    l -= 1
    point = c[r][r]
    point -= c[r][l]
    point -= c[l][r]
    point += c[l][l]
    print(point)