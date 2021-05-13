from sys import stdin, stdout


def solve():
    n,k = [int(i) for i in stdin.readline().split()]
    A = [int(i) for i in stdin.readline().split()]
    dp = [False for _ in range(k + 1)]
    for i in range(1, k+1):
        for j in range(n):
            if A[j] > i: break
            if not dp[i - A[j]]: 
                dp[i] = True
                break
    return "First" if dp[k] else "Second"
print(solve())
