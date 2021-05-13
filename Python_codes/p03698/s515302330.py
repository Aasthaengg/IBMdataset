s = input()

for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j] and i != j:
            print("no")
            exit()
else:
    print("yes")