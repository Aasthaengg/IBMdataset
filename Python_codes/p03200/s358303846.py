s = list(input())
W_count = 0
ans = 0
for i in range(len(s)):
    if s[i] == "W":
        ans += i - W_count
        W_count += 1
print(ans)
