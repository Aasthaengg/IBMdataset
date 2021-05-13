import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    # https://qiita.com/drken/items/dc53c683d6de8aeacf5a#dp-%E5%AE%9F%E8%A3%85%E3%81%AE%E9%A0%86%E5%BA%8F
    
    
    INF = 10**10  # INF+INFを計算してもオーバーフローしない範囲で大きく
    
    N = int(input())
    S=input()
    # dpテーブル dp[i][j]:= ...
    dp = [[0]*N for _ in range(N)]
    
    # 初期条件
    dp[0][0] = 0
    for i in range(N-1):
        if S[i]==S[N-1]:
            dp[N-1][i]=1


    # ループ
    for i in reversed(range(N-1)):
        for j in reversed(range(N-1)):
            if i>j:
                if S[i]!=S[j]:
                    dp[i][j]=0
                else:
                    dp[i][j]=min(i-j,dp[i+1][j+1]+1)
    
    ans=0
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if i>j:
                ans=max(ans,dp[i][j])
    print(ans)

    
    
resolve()