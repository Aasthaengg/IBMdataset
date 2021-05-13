#店1:月1 月2 火1 火曜2...
#店2:月1 ... 金2
#みたいな入力
from itertools import accumulate
n = int(input())
lis = []
for i in range(n):
    A=[int(i) for i in input().split()]
    lis.append(A)
ans = [0]*10
lis2 = []
for i in range(n):
    p = [int(i) for i in input().split()]
    lis2.append(p)

#時間帯bit(i)で営業する場合を見るのでbit全探索
ans = -10000000000
for i in range(1,1<<10):
    kaburi = [0]*n#状態iで店を開く時に被ってる店舗を1~Nごとに記録する　kaburi[i]:店iと何個被ってるか
    tmp = 0
    for j in range(11):
        if(i & 1<<j):
            for k in range(n):
                if lis[k][j]:
                    kaburi[k]+=1
    for j in range(n):
        tmp += lis2[j][kaburi[j]]

    ans = max(tmp, ans)
print(ans)
