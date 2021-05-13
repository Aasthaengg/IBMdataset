import sys
def input(): return sys.stdin.readline().rstrip()
def main():
    h,w=map(int,input().split())
    S=[input() for _ in range(h)]
    L=[[0]*w for _ in range(h)]
    R=[[0]*w for _ in range(h)]
    U=[[0]*w for _ in range(h)]
    D=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if S[i][j]=='#':
                L[i][j]=0
                U[i][j]=0
                continue
            if i==0:U[i][j]=1
            else:U[i][j]=U[i-1][j]+1
            if j==0:L[i][j]=1
            else:L[i][j]=L[i][j-1]+1
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if S[i][j]=='#':
                R[i][j]=0
                D[i][j]=0
                continue
            if i==h-1:D[i][j]=1
            else:D[i][j]=D[i+1][j]+1
            if j==w-1:R[i][j]=1
            else:R[i][j]=R[i][j+1]+1 
    X=[[l+r+u+d-3 for l,r,u,d in zip(ll,rr,uu,dd)] for ll,rr,uu,dd in zip(L,R,U,D)]
    print(max([max(x) for x in X]))


if __name__=='__main__':
    main()