import sys
sys.setrecursionlimit(1000000)

n = int(input())
action = []
for i in range(n):
    action.append(list(map(int,input().split())))

memo = []
for i in range(n):
    memo.append([-1]*3)

def dp(i, a):
    if i == 0:
        return action[0][a]
    elif memo[i][a] != -1:
        return memo[i][a]
    else:
        memo[i][a] = max(dp(i-1, (a+1)%3), dp(i-1, (a+2)%3)) + action[i][a]
        return memo[i][a]

print(max([dp(n-1,a) for a in range(3)]))