import numpy as np
import copy
import itertools
h,w,k = map(int, input().split())
s = [list(input()) for i in range(h)]
data = np.zeros(h*w).reshape(h,w)
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            data[i][j] = 1
 
ans = 0
## 塗らない場合
if np.sum(data == 1) == k:
    ans = 1
## すべて塗った場合
if k == 0:
    ans = 1
 
a = list()
b = list()
for i in range(1,h):
    a += list(itertools.combinations(range(h), i))
for i in range(1,w):
    b += list(itertools.combinations(range(w), i))
 
for i in a:
    for j in b:
        temp = data.copy()
        temp[i,:] = 2
        temp[:,j] = 2
        if np.sum(temp == 1) == k:
            ans += 1
 
for i in a:
    temp = data.copy()
    temp[i,:] = 2
    if np.sum(temp == 1) == k:
        ans += 1
        
for j in b:
    temp = data.copy()
    temp[:,j] = 2
    if np.sum(temp == 1) == k:
        ans += 1
        
print(ans)