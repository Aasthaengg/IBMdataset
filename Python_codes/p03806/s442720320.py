import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,Ma,Mb=map(int,input().split())
    a,b,c=[0]*N,[0]*N,[0]*N
    for i in range(N):
        a[i],b[i],c[i]=map(int,input().split())
    d={}
    ans=INF
    for i in range(2**(N//2)):
        ma,mb,cost=0,0,0
        for j in range(N//2):
            if (i>>j)&1:
                ma+=a[j]
                mb+=b[j]
                cost+=c[j]
        if ma!=0 and mb!=0 and ma*Mb==mb*Ma:
            ans=min(ans,cost)
        n=min(ma//Ma,mb//Mb)
        ma-=n*Ma
        mb-=n*Mb
        if (ma,mb) in d:
            d[(ma,mb)]=min(d[(ma,mb)],cost)
        else:
            d[(ma,mb)]=cost
    for i in range(1,2**(N-N//2)):
        ma,mb,cost=0,0,0
        for j in range(N-N//2):
            if (i>>j)&1:
                ma+=a[j+N//2]
                mb+=b[j+N//2]
                cost+=c[j+N//2]
        n=max(-(-ma//Ma),-(-mb//Mb))
        if (n*Ma-ma,n*Mb-mb) in d:
            ans=min(ans,cost+d[(n*Ma-ma,n*Mb-mb)])
    print(ans if ans!=INF else -1)

if __name__ == '__main__':
    main()
