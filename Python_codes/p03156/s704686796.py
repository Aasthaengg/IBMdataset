n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
dp = [0]*3

for i in p:
    if i <= a:
        dp[0] += 1
    elif a < i <= b:
        dp[1] += 1
    else:
        dp[2] += 1

print(min(dp))