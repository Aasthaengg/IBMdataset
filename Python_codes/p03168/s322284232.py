import sys
import math


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N=int(input())
    P=list(map(float,input().split()))

    dp=[0]*(N+1)
    dp[0]=1
    for j in range(N):
        p =P[j]
        for i in range(N, -1, -1):

            dp[i] = dp[i]*(1-p)
            if i ==0:
                continue
            dp[i] +=dp[i-1] *p

    print(sum(dp[N//2+1:]))






if __name__ == "__main__":
    main()
