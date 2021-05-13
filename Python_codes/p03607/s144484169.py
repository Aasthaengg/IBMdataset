N = int(input())
memo = {}
for i in range(N):
    s = int(input())
    if s in memo:
        memo[s] += 1
    else:
        memo[s] = 1
ans = 0
for key, val in memo.items():
    if val%2:
        ans += 1
print(ans)