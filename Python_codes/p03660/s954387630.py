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

from collections import deque
q = deque()
memo = [-1]*n #0 sente 1: gote
for i in path[:len(path)//2]:
    memo[i] = 1
    q.append(i)
for i in path[len(path)//2:]:
    memo[i] = 0
    q.append(i)

res = len(path)//2 #Sunuke's point

while q: #キューが空になるまで
    v = q.popleft() #キューから情報を取り出す
    for c in g[v]:
        if memo[c] != -1: continue
        #(nx,ny)が未確認のとき、確認済みにしてキューに入れる------------------
        memo[c] = memo[v]
        res += memo[c]
        q.append(c)

if n - res > res: print("Fennec")
else: print("Snuke")





