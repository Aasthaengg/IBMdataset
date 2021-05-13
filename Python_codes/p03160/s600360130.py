import sys
sys.setrecursionlimit(10**5 + 1)
def main():
    global n, peso, dp

    n = int(input())
    peso = [int(x) for x in input().split()]
    dp = [-1]*(10**5 + 1)
    
    peso.append(10**9)
    peso.append(10**9)
    
    print(frog(0))
    
def frog(i):
    global n, peso, dp
    
    if i >= n - 1:
        return 0

    if dp[i] != -1:
        return dp[i]

    dp[i] = min(abs(peso[i + 1] - peso[i]) + frog(i + 1),
                abs(peso[i + 2] - peso[i]) + frog(i + 2))
    
    return dp[i]

main()