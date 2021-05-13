def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    F=list(map(int,input().split()))
    A.sort(reverse=True)
    F.sort()

    l_score=-1
    r_score=10**12
    while l_score<r_score-1:
        t_score=(l_score+r_score)//2
        count=0
        for i in range(N):
            count+=max(0,A[i]-t_score//F[i])
        if count<=K:
            r_score=t_score
        else:
            l_score=t_score
    print(r_score)
if __name__=="__main__":
    main()