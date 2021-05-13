import sys
input=sys.stdin.readline

def main():
    n, k = map(int,input().split())
    H = [0] + list(map(int,input().split()))
    
    dp = [float('inf')]*(n+1)
    dp[1] = 0
    
    for i in range(2,n+1):
        for j in range(1,k+1):
            if i-j <= 0:
                continue
            dp[i] = min(dp[i], abs(H[i]-H[i-j])+dp[i-j])
    
    #print(dp)        
    print(dp[n])
    
if __name__ == '__main__':
    main()