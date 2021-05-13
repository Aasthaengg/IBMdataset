import numpy as np

a = [list(map(int,input().split())) for _ in range(3)]

n = int(input())

b = list([int(input()) for _ in range(n)])

c = np.zeros(9).reshape(3,3)

for k in b:
    for i in range(3):
        for j in range(3):
            if k == a[i][j]:
                c[i,j]=1

if (max(c.sum(axis=0))==3) or (max(c.sum(axis=1))==3) or \
    (sum([c[i,i] for i in range(3)])==3) or (c[2,0]+c[1,1]+c[0,2]==3):
    print("Yes")
else:
    print("No")