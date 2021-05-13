#出来るだけループして端数を全部みるだとうまくいかない（最初と最後に負のスコアが固まっている場合など）

from numba import njit,i8
import numpy as np


n,k = map(int,input().split())
p = np.array([int(i)-1 for i in input().split()],np.int64)
c = np.array(list(map(int,input().split())),np.int64)

@njit(i8(i8,i8[:],i8[:]), cache = True)
def calc_score(x,p,c):
    n = p.size
    score = 0
    score_list = np.zeros(n,np.int64)
    cnt = 0
    visit = [0]*n
    while not visit[p[x]]:
        x = p[x]
        visit[x] = 1
        cnt += 1
        if cnt<=k:
            score += c[x]
            score_list[cnt-1] = score
        else:
            return score_list[:k].max()
    
    if score>0:
        tmp = np.arange(cnt)
        return (score_list[tmp] + ((k-1-tmp)//cnt) * score).max()
    else:
        return score_list[:cnt].max()

ans = max(calc_score(i,p,c) for i in range(n))
print(ans)