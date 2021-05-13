#ABC099-D Good Grid
"""
問題：
条件を満たすようにc色の色を塗り替える場合に生じるコスト(違和感)
を最小化する。
条件：
ある任意の２箇所のグリッド grid[a][b]とgrid[c][d]を見た時に、
(a+b)%3 == (c+d)%3 ならば、その２箇所は同じ色である必要があり、
そうでない場合は違う色である必要がある。
6*6のグラフで見るとこんな感じになる
012012
120120
201201
012012
120120
201201 

解法：
色が30色であるという制約から、
30C3通りを試した時のコストの最小値が答えになる。
500*500のgridで高速に計算する必要があるため、
予めdictを用いて3で割った余りが0,1,2の場所に何の色が何個入っているか
を求めておき、あとはそれぞれの場所から変更先の色へのコストを求めれば
良い。
"""
import sys
from collections import defaultdict
import itertools
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,c = map(int,readline().split()) #N*Nの正方行列,c色
D = [] #隣接リスト(ある色iから色jに塗り替えた時の違和感D[i][j])
#ちなみに、塗り替えなかった場合違和感は0になる
for i in range(c):
    D.append(list(map(int,readline().split())))

grid = [] #元の色のグリッド(1-indexed)
for i in range(n):
    grid.append(list(map(int,readline().split())))



dic_0 = defaultdict(int)
dic_1 = defaultdict(int)
dic_2 = defaultdict(int)

for i in range(n):
    for j in range(n):
        if (i+j)%3 == 0:
            dic_0[grid[i][j]] += 1
        elif (i+j)%3 == 1:
            dic_1[grid[i][j]] += 1
        else:
            dic_2[grid[i][j]] += 1

colors = [i for i in range(1,c+1)]
ans = 10**9
for i,j,k in itertools.combinations(colors,3):
    for o,p,q in itertools.permutations([i,j,k]):
        res = 0
        for a,b in dic_0.items():
            res += D[a-1][o-1]*b
        for a,b in dic_1.items():
            res += D[a-1][p-1]*b
        for a,b in dic_2.items():
            res += D[a-1][q-1]*b

        ans = min(ans,res)

print(ans)
