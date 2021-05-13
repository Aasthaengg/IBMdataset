import sys, os 
sys.setrecursionlimit(10**8)
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

read = lambda : sys.stdin.readline().rstrip('\n')
tint = lambda x: [int(x) for x in x.split()]
inf = float('inf')

def main():
    n = tint(read())[0]
    stones = tint(read())
    dp = [inf]*n
    dp[0] = 0
    for i in range(n-1):
        if i+1 < n:
            dp[i+1] = min(dp[i+1], dp[i]+abs(stones[i]-stones[i+1]))
        if i+2 < n:
            dp[i+2] = min(dp[i+2], dp[i]+abs(stones[i]-stones[i+2]))
    print(dp[-1])


if __name__ == '__main__':    
    main()
