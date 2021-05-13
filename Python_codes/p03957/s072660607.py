s = list(input())

for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == "C" and s[j] == "F" and i<j:
            print("Yes")
            exit()
print("No")