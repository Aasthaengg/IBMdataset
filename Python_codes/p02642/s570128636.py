n = int(input())
a = list(map(int,input().split()))

a = sorted(a)
max_a = max(a)
dp = [1 for i in range(max_a+1)]
a_num = [0 for i in range(max_a+1)]
ans = 0

for i in a:
    a_num[i] += 1
    if a_num[i] == 2:
        tmp = i
        while tmp+i <= max_a:
            tmp += i
            dp[tmp] = 0
        dp[i] = 0

for i in a:
    if dp[i] == 0:
        continue
    else:
        ans += 1
        tmp = i
        while tmp+i <= max_a:
            tmp += i
            dp[tmp] = 0

print(ans)
