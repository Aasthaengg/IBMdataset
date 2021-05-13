# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:22:54 2020

@author: Maruthi Srinivas
"""
import sys
sys.setrecursionlimit(1000000)
def dfs(node,graph,dp):
    temp=0
    if dp[node]!=-1:
        return dp[node]
    for i in graph[node]:
        temp=max(temp,dfs(i,graph,dp)+1)
    dp[node]=temp
    return temp
            
v,e=map(int,input().split())
adj={x:[] for x in range(v+1)}
for i in range(e):
    x,y=map(int,input().split())
    adj[x].append(y)
m=-1
dp=[-1]*(v+1)
for i in range(1,v+1):
    x=dfs(i,adj,dp)
    m=max(m,x)
print(m)

