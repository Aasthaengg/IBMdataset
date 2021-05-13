s=input()
c=0
for i in range(len(s)):
    if i % 2 == 0 and s[i] in ["R","U","D"]:
        c += 1
    elif i % 2 == 1 and s[i] in ["L","U","D"]:
        c += 1
print("Yes" if c == len(s) else "No")