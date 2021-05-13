import sys
input = lambda: sys.stdin.readline().rstrip()

match_dict = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

N,M = map(int, input().split())
A = list(map(int, input().split()))

def greater(a, b):
    if len(a) == len(b):
        return max(a, b)
    elif len(a) > len(b):
        return a
    else:
        return b        

dp = ["0"] * 11000

dp[0] = "" 

for i in range(N+1):
    
    for a in A:
        if i - match_dict[a] >= 0 and dp[i-match_dict[a]] != '0':
            dp[i] = greater(dp[i - match_dict[a]] + str(a), dp[i])

print(dp[N])