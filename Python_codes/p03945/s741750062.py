import sys

s = input()

before = s[0]
ans = 0
for cx in range(1, len(s)):
    if before != s[cx]:
        ans += 1
        before = s[cx]

print(ans)
