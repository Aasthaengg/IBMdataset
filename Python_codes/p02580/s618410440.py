from collections import deque,defaultdict
import heapq as hp
def solve():
    h,w,m=map(int,input().strip().split(" "))
    dr=defaultdict(int)
    dc=defaultdict(int)
    s=set()
    for _ in range(m):
        a,b=map(int,input().strip().split(" "))
        dr[a]+=1
        dc[b]+=1
        s.add((a,b))

    kr=max(dr.values())
    kc=max(dc.values())
    rs=[]
    cs=[]
    rs+=[i for i in dr.keys() if dr[i]==kr ]
    cs+=[i for i in dc.keys() if dc[i]==kc ]
    for i in rs:
        for j in cs:
            if (i,j) not in s:
                print(kr+kc)
                exit()

    print(kr+kc-1)






solve()
