from collections import defaultdict as dd
s = input()
#dp[keta][amari] = pattern_num
dp = dd(lambda: dd(lambda: 0))
nums = list(range(0, 10))

for keta in range(1, len(s)+1):
    digit = s[keta-1]
    if digit != "?":
        digit = int(digit)
        if keta == 1:
            dp[keta][digit] = 1
        else:
            for amari, val in dp[keta-1].items():
                dp[keta][(amari * 10 + digit) % 13] += val
                dp[keta][(amari * 10 + digit) % 13] %= 10**9 + 7

    else:
        if keta == 1:
            for digit in nums:
                dp[keta][digit] = 1
        else:
            for digit in nums:
                for amari, val in dp[keta-1].items():
                    dp[keta][(amari * 10 + digit) % 13] += val
                    dp[keta][(amari * 10 + digit) % 13] %= 10**9 + 7

print(dp[len(s)][5] % (10**9 + 7))