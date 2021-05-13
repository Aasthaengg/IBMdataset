import sys 
sys.setrecursionlimit(2147483647)

memo = [float("inf")]*100005

def rec(n):
    if n==0:
        return 0
    if memo[n]!=float("inf"):
        return memo[n]
    res = float("inf")
    val = 1
    while val<=n:
        res = min(res,rec(n-val)+1)
        val*=6
    
    val = 1
    while val<=n:
        res = min(res,rec(n-val)+1)
        val*=9
    memo[n]=res
    return memo[n]

if __name__ == "__main__":
    N = int(input())
    print(rec(N))