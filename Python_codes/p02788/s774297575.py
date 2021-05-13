import sys
input=sys.stdin.readline
from bisect import bisect_right

def main():
    n,d,a=map(int,input().split())
    XH=[list(map(int,input().split())) for _ in range(n)]
    XH.sort()
    X=[i[0] for i in XH]
    Damage=[0]*(n+1)
    ans=0
    for i,(x,h) in enumerate(XH):
        Damage[i]+=Damage[i-1]
        h-=Damage[i]
        if h<=0:
            continue
        cnt=(h+a-1)//a
        ans+=cnt
        Damage[i]+=a*cnt
        br=bisect_right(X,x+2*d)
        Damage[br]-=a*cnt
    print(ans)
    
if __name__=='__main__':
    main()