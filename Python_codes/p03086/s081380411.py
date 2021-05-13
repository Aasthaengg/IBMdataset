s = input()
ans = 0
total = 0
for i in range(len(s)):
    if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
        total += 1
        if total > ans:
            ans = total
    else:
        total = 0
print(ans)