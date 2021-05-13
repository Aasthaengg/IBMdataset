if __name__ == '__main__':
    import sys
    input=sys.stdin.readline
    N,Q=list(map(int,input().split()))
    events=[list(map(int,input().split())) for _ in range(N)]
    D=[int(input()) for i in range(Q)]
    ans=["-1"]*Q
    skip=[-1]*Q
    events.sort(key=lambda x:x[2])
    import bisect
    for S,T,X in events:
        right=bisect.bisect_left(D,T-X)
        left=bisect.bisect_left(D,S-X)
        while left<right:
            if skip[left]==-1:
                ans[left]=str(X)
                skip[left]=right
                left+=1
            else:
                left=skip[left]
    print("\n".join(ans))
