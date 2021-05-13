s = input()
ans = []
for i in range(len(s)):
    if i == 5 or i == 13:
        ans.append(" ")
    else:
        ans.append(s[i])
print("".join(map(str, ans)))