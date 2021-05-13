# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n = int(input())

g = [[] for _ in range(n)]
for i in range(n-1):
    a,b = [int(i) for i in readline().split()]
    g[a-1].append(b-1)
    g[b-1].append(a-1)

"""
def dfs(v,p,path):
    for c in g[v]:
        if c == p: continue
        if c == n-1:
            path.append(n-1)
            path.append(v)
            return True
        if dfs(c,v,path):
            path.append(v)
            return True
    return False            

path = []
dfs(0,-1,path)
path.reverse()
"""


from collections import deque

def bfs(g,root,memo):
    q = deque()
    #memo = [-1]*n: あらかじめ初期化しておく
    """初期化、キューに入れて使用済みにする"""
    memo[root] = 0
    q.append(root)
    """BFS"""
    while q: #キューが空になるまで
        v = q.popleft() #キューから情報を取り出す
        for c in g[v]:
            if memo[c] != -1: continue #確認済みならスキップ
            # 確認済みにしてキューに入れる
            memo[c] = memo[v] + 1
            q.append(c)

memo0 = [-1]*n
memo1 = [-1]*n

bfs(g,0,memo0)
bfs(g,n-1,memo1)

ans = 0
for i,j in zip(memo0,memo1):
    if i <= j: ans += 1

#print(memo0)
#print(memo1)

if ans > n - ans: print("Fennec")
else: print("Snuke")







