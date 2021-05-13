import sys
import math


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    H,W =map(int,input().split())
    A =[]
    mod =10**9+7
    for i in range(H):
        a =list(input())
        A.append(a)

    dp =[[0] *W for _ in range(H)]
    dp[0][0]=1
    for i in range(H):
        for j in range(W):
            if j+1<W and A[i][j+1]==".":
                dp[i][j+1] +=dp[i][j]
            if i+1<H and A[i+1][j] ==".":
                dp[i+1][j] +=dp[i][j]
                dp[i+1][j] %=mod

    print(dp[H-1][W-1]%mod)





if __name__ == "__main__":
    main()
