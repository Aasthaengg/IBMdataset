s = input()
n = len(s)
i = 0
j = 0
ans = 0
while i < n:
    if s[i] == "A":
        j += 1
        i += 1
    elif i + 1 < n and s[i:i + 2] == "BC":
        ans += j
        i += 2
    else:
        j = 0
        i += 1
print(ans)
