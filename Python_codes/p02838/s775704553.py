from collections import Counter 
from collections import defaultdict
from collections import deque
from functools import reduce
import math
import itertools
import heapq
import bisect
import sys
#import sympy
sys.setrecursionlimit(10**6)


def bfs(s,n,node):
    #頂点が探索済みかどうかのチェック配列
    check=[False for _ in range(n)]
    check[s]=True
    #次見る頂点を格納するキュー
    queue=deque([s])
    visited_num=1

    #問題固有の配列
    #color_check=[[True for _ in range(l)] for _ in range(n)]
    color=[-1 for _ in range(n)]
    color[s]=0
    
    while visited_num<n:
        #グラフが全連結ではない場合
        if len(queue)==0:
            #空配列を返す
            #現状までの計算済み配列を返してもいいと思う
            return color

        now_vertex=queue.popleft()
        #インデックスがない場合は
        for next_vertex in node[now_vertex]:


            if check[next_vertex]==True:
                continue

            queue.append(next_vertex)
            check[next_vertex]=True

            #問題固有の計算
            color[next_vertex]=color[now_vertex]+1
            visited_num+=1

    return color

#n=int(input())z
#n,m=list(map(int,input().split()))
#a=list(map(int,input().split()))
ceil=lambda x,y: (x+y-1)//y
input_list = lambda : list(map(int,input().split()))



n=int(input())
#n,m=input_list()
a=input_list()
f_num=60
z_arr=[0 for _ in range(f_num)]
o_arr=[0 for _ in range(f_num)]
#a=[bin(i)[2:].zfill(f_num) for i in tmp]
for each in a:
    cal=bin(each)[2:].zfill(f_num)
    for i in range(f_num):
        if (cal[i])=="0":
            z_arr[i]+=1
        else:
            o_arr[i]+=1
mod=10**9+7
ans=0



for keta_i in range(f_num):
    cal=((z_arr[keta_i]*o_arr[keta_i])%mod*pow(2,f_num-keta_i-1,mod))%mod
    ans+=cal
    ans%=mod

ans%=mod
print(ans)