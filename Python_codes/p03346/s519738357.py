n = int(input())
a = [int(input()) for i in range(n)]

memo = {}
for i in range(n):
    memo[a[i]] = i
ans = 0
pos = -1
cnt = 0
for i in range(n):
    if pos < memo[i+1]:
        cnt += 1
        pos = memo[i+1]
    else:
        ans = max(ans, cnt)
        cnt = 1
        pos = memo[i+1]
print(n - max(ans, cnt))
