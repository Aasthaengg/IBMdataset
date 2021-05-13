from collections import deque
def main():
    N = int(input())
    divs = [59049, 46656, 7776, 6561, 1296, 729, 216, 81, 36, 9, 6, 1]
    dp = [0]*(10**6+1)
    def f(x):
        if x == 0:
            return 0
        if x < 0:
            return 10**6
        if dp[x]:
            return dp[x]
        else:
            res = 10**6
            for d in divs:
                res = min(res,f(x-d)+1)
            dp[x] = res
            return res
            

    print(f(N))
main()