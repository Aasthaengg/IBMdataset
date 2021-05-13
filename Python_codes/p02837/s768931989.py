from itertools import product
N = int(input())
A = []
XY = []
for i in range(N):    
    a = int(input())
    A.append(a)
    xy = [list(map(int,input().split())) for _ in range(a)]
    XY.append(xy)
flag = 0
ans = 0
for i in product((0,1), repeat=N):
    for idx, j in enumerate(i):
        if j:
            for x, y in XY[idx]:
                if i[x-1] != y:
                    flag = 1
                if flag:
                    break
        if flag:
            break
    if flag == 0:
        ans = max(ans, sum(i))
    if flag:
        flag = 0
print(ans)