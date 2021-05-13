s = input()
flag = 0
ans = "No"

for i in range(len(s)):
    if s[i] == "C":
        flag = 1

    if flag == 1 and s[i] == "F":
        ans = "Yes"
        break

print(ans)