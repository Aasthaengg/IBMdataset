s = input()
len_s = len(s)
w = list("keyence")

ans = "NO"
if s[0:7] == "keyence":
    ans = "YES"
elif s[0] == "k" and s[len_s-6:] == "eyence":
    ans = "YES"
elif s[0:2] == "ke" and s[len_s-5:] == "yence":
    ans = "YES"
elif s[0:3] == "key" and s[len_s-4:] == "ence":
    ans = "YES"
elif s[0:4] == "keye" and s[len_s-3:] == "nce":
    ans = "YES"
elif s[0:5] == "keyen" and s[len_s-2:] == "ce":
    ans = "YES"
elif s[0:6] == "keyenc" and s[len_s-1:] == "e":
    ans = "YES"
elif s[len_s-7:] == "keyence":
    ans = "YES"

print(ans)