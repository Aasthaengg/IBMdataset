s = input()
yes = False
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] == "C" and s[j] == "F":
            yes = True
            break
    if yes:
        break
        
if yes:
    print("Yes")
else:
    print("No")