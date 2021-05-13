def main():
    from itertools import accumulate as ac
    n,c=map(int,input().split())
    xv=[list(map(int,input().split())) for _ in [0]*n]
    rmemo=[0]*n
    lmemo=[0]*n
    rmemo[0]=xv[0][1]-xv[0][0]
    lmemo[n-1]=xv[n-1][1]-(c-xv[n-1][0])
    for i in range(1,n):
        rmemo[i]=rmemo[i-1]+xv[i][1]-xv[i][0]+xv[i-1][0]
    for i in range(n-2,-1,-1):
        lmemo[i]=lmemo[i+1]+xv[i][1]+xv[i][0]-xv[i+1][0]
    temp=rmemo[0]
    rmemo2=[temp]*(n)
    temp=lmemo[-1]
    lmemo2=[temp]*(n+1)
    lmemo2[-1]=0
    for i in range(1,n):
        rmemo2[i]=max(rmemo[i],rmemo2[i-1])
    for i in range(n-2,-1,-1):
        lmemo2[i]=max(lmemo[i],lmemo2[i+1])
    rmemo2=[0]+rmemo2
    ans=max(rmemo+lmemo+[0])
    for i in range(n):
        ans=max(ans,rmemo[i]+lmemo2[i+1]-xv[i][0])
        ans=max(ans,lmemo[i]+rmemo2[i]+xv[i][0]-c)
    print(ans)
main()