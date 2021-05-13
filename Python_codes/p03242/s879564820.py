s = list(str(input()))
ans = ""
for i in range(3):
    if s[i] == "1":
        ans = ans + "9"
    else:
        ans = ans + "1"
print(ans)
