import sys;sys.setrecursionlimit(10**6)
    #双方向に連結しろ！！！！！！！
from collections import *
    #双方向に連結しろ！！！！！！！
d=defaultdict(list)
    #双方向に連結しろ！！！！！！！
n=int(input())
    #双方向に連結しろ！！！！！！！
start=2
    #双方向に連結しろ！！！！！！！
for i in range(n-1):
    #双方向に連結しろ！！！！！！！
    a,b=map(int,input().split())
    #双方向に連結しろ！！！！！！！
    d[a].append(b)
    #双方向に連結しろ！！！！！！！
    d[b].append(a)
    #双方向に連結しろ！！！！！！！
    start=min(start,a)
    #双方向に連結しろ！！！！！！！
*p,=sorted(map(int,input().split()))
    #双方向に連結しろ！！！！！！！
ans=[0 for i in range(n)]
    #双方向に連結しろ！！！！！！！
def DFS_dict(point,TFlist):
    #双方向に連結しろ！！！！！！！
    if all(TFlist):
    #双方向に連結しろ！！！！！！！
        return 1
    #双方向に連結しろ！！！！！！！
    for i in d[point]:
    #双方向に連結しろ！！！！！！！
        if TFlist[i-1]:
    #双方向に連結しろ！！！！！！！
            continue
    #双方向に連結しろ！！！！！！！
        TFlist[i-1]=True
        ans[i-1]=p.pop()
    #双方向に連結しろ！！！！！！！
        DFS_dict(i,TFlist)
    #双方向に連結しろ！！！！！！！
        TFlist[i-1]=False
    #双方向に連結しろ！！！！！！！
    return ans
    #双方向に連結しろ！！！！！！！
TFlist=[False]*n
    #双方向に連結しろ！！！！！！！
TFlist[start-1]=True
    #双方向に連結しろ！！！！！！！
score=sum(p)-max(p)
    #双方向に連結しろ！！！！！！！
ans[start-1]=p.pop()
    #双方向に連結しろ！！！！！！！
ans=DFS_dict(start,TFlist)
    #双方向に連結しろ！！！！！！！
print(score)
    #双方向に連結しろ！！！！！！！
print(*ans)