S = input()
'''
dp[i]はSのi文字目（1~Sの長さ)までを表せるかどうか
'''
dp = [0] * (len(S) + 1)
dp[0] = 1
check = "NO"

words = ["dream", "dreamer", "erase", "eraser"]

for i in range(len(S)):
    if dp[i] == 0:
        continue
    for w in words:
        if S[i:i+len(w)] == w:
            dp[i+len(w)] = 1
    if dp[len(S)] == 1:
        check = "YES"
        break

print(check)
