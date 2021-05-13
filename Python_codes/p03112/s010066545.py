def main():
    INF=10**11
    from bisect import bisect_left
    a,b,q=map(int,input().split())
    S=[-INF]+[int(input()) for _ in range(a)]+[INF]
    T=[-INF]+[int(input()) for _ in range(b)]+[INF]

    for _ in range(q):
        x=int(input())
        s=bisect_left(S,x)
        t=bisect_left(T,x)
        ans=max(T[t],S[s])-x
        ans=min(ans,S[s]-T[t-1]+min(S[s]-x,x-T[t-1]))
        ans=min(ans,x-min(S[s-1],T[t-1]))
        ans=min(ans,T[t]-S[s-1]+min(T[t]-x,x-S[s-1]))
        print(ans)
if __name__=='__main__':
    main()