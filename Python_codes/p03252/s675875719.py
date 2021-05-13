s = input()
t = input()
R1 = {i:-1 for i in "abcdefghijklmnopqrstuvwxyz"}
R2 = {i:-1 for i in "abcdefghijklmnopqrstuvwxyz"}
for i in range(len(s)):
    if R1[s[i]] != -1:
        if R1[s[i]] != t[i]:
            print("No")
            break
    else:
        R1[s[i]] = t[i]
    if R2[t[i]] != -1:
        if R2[t[i]] != s[i]:
            print("No")
            break
    else:
        R2[t[i]] = s[i]
else:
    print("Yes")