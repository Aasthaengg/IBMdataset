import copy
#import time

h,w = map(int,input().split())
a = [input() for _ in range(h)]
b = [[False]*w for _ in range(h)]
#s = time.time()
c = []
d = [(-1,0), (1,0), (0,-1), (0,1)]
ans = 0

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            b[i][j] = True
            c.append((i,j))
#print(time.time()-s)

while True:
    tmp = []
    cnt = 0
    for i,j in c:
        for d1,d2 in d:
            if 0 <= i + d1 < h and 0 <= j + d2 < w:
                if not b[i+d1][j+d2]:
                    tmp.append((i+d1, j+d2))
                    b[i+d1][j+d2] = True
                    cnt += 1
    #print(time.time()-s)
    if cnt > 0:
        c = copy.copy(tmp)
        ans += 1
    else:
        break
    #print(time.time()-s)

print(ans)
