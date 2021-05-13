import sys
sys.setrecursionlimit(10**6)
from sys import stdin
input = stdin.readline

n = int(input())
adjacency = [[] for i in range(n+1)] #adjacency[i]は頂点iと隣接する頂点のリスト
distance = {} # distance[(i,j)](i,jは隣接した頂点)は頂点i,jを結ぶ辺の長さ
for i in range(n-1):
    line = list(map(int, input().split()))
    adjacency[line[0]].append(line[1])
    adjacency[line[1]].append(line[0])
    distance[(line[0], line[1])] = line[2]
    distance[(line[1], line[0])] = line[2]
q, k = map(int, input().split())
x = []
y = []
for i in range(q):
    line = list(map(int, input().split()))
    x.append(line[0])
    y.append(line[1])

k_distance = [-1 for i in range(n+1)] # k_distance[i]は頂点i,kの距離
k_distance[k] = 0
reached = {k}
def dfs(v, d): # 現在いる頂点vと頂点v,k間の距離dを入力すると頂点vと隣接する未到達の頂点のk_distanceを計算してappendする
    for neighbor in adjacency[v]:
        if not neighbor in reached:
            reached.add(neighbor)
            k_distance[neighbor] = d + distance[(v, neighbor)]
            dfs(neighbor, k_distance[neighbor])
    return
dfs(k, 0)
for i in range(q):
    print(k_distance[x[i]] + k_distance[y[i]])
