import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

A = list(map(int, input().split()))

match_dict = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

dp = ["0"] * 10010

dp[0] = ""

def greater(x, y):
    if len(x) == len(y):
        return max(x, y)
    else:
        return x if len(x) > len(y) else y

for i in range(N):
    if dp[i] != "0":
        for num in A:
            dp[i+match_dict[num]] = greater(dp[i+match_dict[num]], dp[i]+str(num))

print(dp[N])