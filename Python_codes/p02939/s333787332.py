s = input()

dp = [[[0, ''], [0, '']], [[1, s[0]], [-10**6, '']]]
for i in range(1, len(s)):
    if s[i-1:i+1] == dp[-2][1][1]:
        ndp1 = [dp[-2][0][0]+1, s[i-1:i+1]]
    else:
        ndp1 = [max(dp[-2][0][0], dp[-2][1][0])+1, s[i-1:i+1]]
    if s[i] == dp[-1][0][1]:
        ndp0 = [dp[-1][1][0]+1, s[i]]
    else:
        ndp0 = [max(dp[-1][0][0], dp[-1][1][0])+1, s[i]]
    dp.append([ndp0, ndp1])

print(max(dp[len(s)][0][0], dp[len(s)][1][0]))