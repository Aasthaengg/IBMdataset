import sys
import heapq
def v():
    N,T=tuple(map(int,sys.stdin.readline().split()))
    A=list(map(int,sys.stdin.readline().split()))
    ma=0
    d=[]
    heapq.heapify(d)
    for a in reversed(A):
        if a<ma:heapq.heappush(d,a-ma)
        else:ma=a
    res,x=1,heapq.heappop(d)
    while len(d)>0:
        y=heapq.heappop(d)
        if x==y:res+=1
    print(res)
if __name__=='__main__':v()