n = int(input())
a = sorted(list(map(int, input().split())))

a_max = a[-1]
dp = [1]*a_max

for i in set(a):
    j = 2
    while i*j <= a_max:
        dp[i*j-1] = 0
        j += 1

a.append(0)
ans = 0
for i in range(n):
    if dp[a[i]-1] and a[i-1] != a[i] and a[i] != a[i+1]:
        ans += 1
print(ans)
