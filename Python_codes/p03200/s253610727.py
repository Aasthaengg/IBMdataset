s = input()

w = 0
ans = 0

for i in range(len(s)):
    if s[i] == "W":
        w += 1
        ans += i+1-w

print(ans)
