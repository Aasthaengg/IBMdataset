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
path.reverse()

#print(path)

from collections import deque
#0 sente 1: gote
q0 = deque()
q1 = deque()
ans = [-1]*n
for i in path[:(1+(len(path)))//2]:
    ans[i] = 0
    q0.append(i)
for i in path[(1+(len(path)))//2:]:
    ans[i] = 1
    q1.append(i)

turn = len(path)&1

while q0 and q1: #キューが空になるまで
    if turn: v = q1.popleft() #キューから情報を取り出す
    else: v = q0.popleft()
    for c in g[v]:
        if ans[c] != -1: continue
        #(nx,ny)が未確認のとき、確認済みにしてキューに入れる------------------
        ans[c] = turn
        if turn: q1.append(c)
        else: q0.append(c)
    turn ^= 1

if q0: print("Fennec")
else: print("Snuke")











