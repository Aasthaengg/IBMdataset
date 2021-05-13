s = input()
C = False

for i in range(len(s)):
    if s[i] == "C":
        C = True
    elif C and s[i] == "F":
        print("Yes")
        exit()

print("No")
