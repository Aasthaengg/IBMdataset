# 第2回全国統一プログラミング王決定戦予選-A
if False:
    N=int(input())
    if N%2==0: print(N//2-1)
    else: print(N//2)

# 第1回同じ-A
if False:
    M,D=map(int,input().split())
    ans=0
    for m in range(1,M+1):
        for d in range(1,D+1):
            if len(str(d))==2:
                x,y=int(str(d)[0]),int(str(d)[1])
                if x>=2 and y>=2 and x*y==m:
                    ans+=1
    print(ans)

#d2019PC2 - A
if False:
    N,K=map(int,input().split())
    MAX=N-K+1
    print(MAX-1 if K!=1 else 0)

#https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_a
if True:
    N,A,B=map(int,input().split())
    MAX=min(A,B)
    MIN=A+B-N if A+B>=N else 0
    print(MAX,MIN)
