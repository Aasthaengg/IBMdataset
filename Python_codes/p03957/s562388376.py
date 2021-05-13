s = input()
ans = "No"
for i in range(len(s)):
    for j in range(len(s)):
        if i < j and s[i] == "C" and s[j] == "F":
            ans = "Yes"
print(ans)
