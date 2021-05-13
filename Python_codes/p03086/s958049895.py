s = list(input())
right = 0
ans = 0
for left in range(len(s)):
    while right < len(s) and s[right] in ["A", "C", "G", "T"]:
        right += 1
    ans = max(ans, right - left)
    right = left + 1
print(ans)