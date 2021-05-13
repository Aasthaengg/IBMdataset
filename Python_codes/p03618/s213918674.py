s = input()

memo = {}
ans = 0

for i in range(len(s)):
    if s[i] not in memo:
        memo[s[i]] = 1
    else:
        memo[s[i]] += 1
    ans += (i+1) - memo[s[i]]

print(ans + 1)