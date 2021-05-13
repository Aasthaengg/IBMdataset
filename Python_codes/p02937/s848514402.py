import bisect
s = input()
t = input()
sub = s+s
dp = []
for i in range(len(s)):
    d = [10**15]*26
    dp.append(d)
index = [[] for i in range(26)]
for i in range(len(sub)):
    index[ord(sub[i])-97].append(i)
for i in range(len(s)):
    cur = s[i]
    for j in range(26):
        if len(index[j]) != 0:
            k = bisect.bisect_right(index[j], i)
            dp[i][j] = index[j][k]-i
if s[0] == t[0]:
    ans = 1
else:
    ans = dp[0][ord(t[0])-97]+1
if dp[0][ord(t[0])-97] != 10**15 and dp[0][ord(t[0])-97] >= len(s):
    next = dp[0][ord(t[0])-97]-len(s)
else:
    next = dp[0][ord(t[0])-97]
if next == 10**15:
    print(-1)
    exit()
else:
    flag = True
for i in range(1,len(t)):
    cur = next
    if dp[cur][ord(t[i])-97] == 10**15:
        flag = False
        break
    else:
        ans += dp[cur][ord(t[i])-97]
        if cur + dp[cur][ord(t[i])-97] >= len(s):
            next = cur + dp[cur][ord(t[i])-97] - len(s)
        else:
            next = cur + dp[cur][ord(t[i])-97]
if flag:
    print(ans)
else:
    print(-1)
