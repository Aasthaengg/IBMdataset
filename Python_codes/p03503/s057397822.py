n = int(input())
fl = [list(map(int, input().split())) for _ in range(n)]
pl = [list(map(int, input().split())) for _ in range(n)]

import itertools

xl = list(itertools.product(range(2), repeat=10))

res = -1*(10**10)

for i in range(1,1024):# 開店パターン
    temp =0
    for j in range(n):#　店の数
        op = 0
        
        for k in range(10):#掛け算して営業タイミング確認
            op += xl[i][k]*fl[j][k] 
        temp += pl[j][op]
    
    res = max(res,temp)
    
print(res)