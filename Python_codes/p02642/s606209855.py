import collections

n = int(input())
a = list(map(int,input().split()))
cnt = collections.Counter(a)
#print(cnt)
a.sort()
dp = [1]*(max(a)+1)

sum = 0
for i in range(n):
    for j in range(a[i]*2,len(dp),a[i]):
            dp[j] = 0
    if dp[a[i]] == 1 and cnt[a[i]]==1:
        sum += 1

print(sum)