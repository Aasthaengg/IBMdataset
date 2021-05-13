# int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
# [int(i) for i in input().split()] # 配列で数字

def nC2(n):
    return n * (n - 1) // 2
s = input()
n = len(s)
dp = [0] * 2020
mod = 2019
temp = 0
dp[0] = 1
for i in range(n):
    m = (int(s[i]) * pow(10, n - i - 1, mod) + temp)% mod
    dp[m] += 1
    temp = m
ans = 0
for i in range(2020):
    if dp[i]:
        ans += nC2(dp[i])
print(ans)