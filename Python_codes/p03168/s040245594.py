import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N = int(input())
    a = list(map(float,input().split()))
    ha = -(-N//2)
    
    dp = np.zeros(N+1,dtype=float)
    dp[0] = 1
    for num in a:
        front = np.zeros(N+1,dtype=float)
        front[1:] = dp[:-1]*num
        dp *= (1-num)
        dp += front
    
    print(np.sum(dp[ha:]))
    
if __name__ == "__main__":
    main()
