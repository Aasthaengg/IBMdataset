s = input()

for i in range(len(s)):
    if s[i] == "C":
        break
    elif i == len(s) - 1:
        print("No")

if i != len(s) - 1:
    for j in range(i, len(s)):
        if s[j] == "F":
            print("Yes")
            break
        elif j == len(s) - 1:
            print("No")