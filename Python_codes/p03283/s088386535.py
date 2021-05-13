import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    # https://atcoder.jp/contests/abc005/tasks/abc005_4
    # https://qiita.com/drken/items/56a6b68edef8fc605821#4-%E4%BA%8C%E6%AC%A1%E5%85%83%E7%B4%AF%E7%A9%8D%E5%92%8C
    # https://upura.hatenablog.com/entry/2019/04/01/212701
    N,M,Q=map(int,input().split())
    D=[[0]*N for _ in range(N)]
    for i in range(M):
        l,r=map(int,input().split())
        l-=1
        r-=1
        D[l][r]+=1

    
    # 2次元累積和
    # S[x][y]:= [0:x] * [0:y]の長方形区間の和
    S = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j] + D[i][j]
    
    for i in range(Q):
        p,q=map(int,input().split())
        x1,y1=p-1,p-1
        x2,y2=q,q
        ans=S[x2][y2] - S[x1][y2] - S[x2][y1] + S[x1][y1]
        print(ans)
    
    
    
    
resolve()