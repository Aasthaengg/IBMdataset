import re
s = input()
ans = [-1] * (len(s) + 1)
if s[0] == '<':
    ans[0] = 0
    diff = 1
    while (0 <= diff -1 < len(s)):
        if (s[diff - 1] == '>'):
            break
        ans[diff] = max(ans[diff], ans[diff - 1] + 1)
        diff += 1
        
if s[len(s) - 1] == '>':
    t = len(s)
    ans[t] = 0
    diff = -1
    while (0 <= t + diff < len(s)) & (s[t + diff] == '>'):
        ans[t + diff] = max(ans[t + diff], ans[t + diff + 1] + 1)
        diff -= 1

match = []
for i in range(len(s)):
    if s[i:i+2] == '><':
        match.append(i)

for i in match:
    ans[i + 1] = 0
    diff = 1
    while (0 <= i + 1 - diff < len(s)):
        if s[i - diff + 1] == '<':
            break
        ans[i + 1 - diff] = max(ans[i + 1 - diff], ans[i - diff + 2] + 1)
        diff += 1
    diff = 1
    while (0 <= i + diff < len(s)):
        if s[i + diff] == '>':
            break
        ans[i + 1 + diff] = max(ans[i + 1 + diff], ans[i + diff] + 1)
        diff += 1
print(sum(ans))