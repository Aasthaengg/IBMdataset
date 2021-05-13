n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = 2**40

dp = [0, 0]

flag = True
while b>0:
    dp2 = dp[:]
    c = 0
    d = 0
    for i in a:
        if (i & b) == 0:
            c += 1
        else:
            d += 1
    if (k & b) == 0:
        if not flag:
            dp[0] = dp2[0]+max(c, d) * b
            dp[1] += d * b
        else:
            dp[1] += d * b
    else:
        if not flag:
            dp[0] = max(dp2[0]+max(c, d) * b, dp2[1]+d * b)
            dp[1] += c * b
        else:
            dp[0] += d*b
            dp[1] += c * b
            flag = False
        
    b //= 2

print(max(dp))
