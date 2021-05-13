'''
1 1 1
2 2 2
1
2
3
とあったら、1*1+1*2+1*3
          2*1+2*2+2*3
みたいな感じ。
'''

from operator import add
from functools import reduce

#テスト値
n,m = map(int,input().split())
#a = [[1,1,1],[2,2,2]]
#b = [1,2,3]

a = [list(map(int, input().split())) for n in range(n)]
#print(a)

b = [int(input()) for n in range(m)]
#print(b)

#ベクトル積の計算。
#まず行ごとの値を計算。
c = []
for n in range(n):
    c.append([a[n][m]*b[m] for m in range(m)])
    
#print(c)#ここまでOK。

d=[reduce(add,c[n]) for n in range(len(c))]



#print(d)

[print(d[i]) for i in range(len(d))]

