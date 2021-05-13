#editorial参照
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split( ))
Ad = [[[] for _ in range(3)] for i in range(n)]

#移動回数込みで移動可能かの情報をグラフの接続として記録
for i in range(m):
    ui,vi = map(int,input().split( ))
    ui -= 1
    vi -= 1
    Ad[ui][0].append((vi,1))
    Ad[ui][1].append((vi,2))
    Ad[ui][2].append((vi,0))


s,t = map(int, input().split( ))
s -= 1
t -= 1
Q = deque()
Q.append((s,0))
Visit = [[-1 for _ in range(3)] for i in range(n)]
Visit[s][0] = 0
while Q:
    v,i = Q.popleft()
    for u,j in Ad[v][i]:
        if Visit[u][j]<0:
            Visit[u][j] = Visit[v][i] + 1
            Q.append((u,j))
        if u==t and j==0:
            Q.clear()
            break
#print(Visit)
print(Visit[t][0]//3)