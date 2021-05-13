import sys
from heapq import heappush,heappop,heapify
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
    sushies=[]
    for i in range(N):
        t,d=map(int,input().split())
        sushies.append((d,t-1))
    sushies.sort()
    b=[False]*N
    overlappedsushi=[]
    ans=0
    n=0
    for i in range(K):
        sushi=sushies.pop()
        if b[sushi[1]]:
            heappush(overlappedsushi,sushi)
            ans+=sushi[0]
        else:
            b[sushi[1]]=True
            ans+=sushi[0]
            n+=1
    ans+=n**2
    tmp=ans
    while overlappedsushi:
        worstsushi=heappop(overlappedsushi)
        tmp-=worstsushi[0]
        while sushies:
            bestsushi=sushies.pop()
            if not b[bestsushi[1]]:
                break
        else:
            break
        n+=1
        tmp+=bestsushi[0]
        tmp+=n*2-1
        b[bestsushi[1]]=True
        ans=max(ans,tmp)
    print(ans)

    

if __name__ == '__main__':
    main()
