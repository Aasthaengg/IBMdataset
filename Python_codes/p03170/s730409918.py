import sys
def main():
    N,K=tuple(map(int,sys.stdin.readline().split()))
    a=tuple(map(int,sys.stdin.readline().split()))
    dp=[False for _ in range(K+1)]
    for i in range(K+1):
        for x in a:
            if i-x>=0:dp[i]=dp[i] or (not dp[i-x])
    print('First') if dp[K] is True else print('Second')
if __name__=='__main__':main()