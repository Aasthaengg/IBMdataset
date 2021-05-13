import sys

s = input()
for i in range(len(s)):
    for j in range(len(s)):
        if i != j and s[i]==s[j]:
            print("no")
            sys.exit()
print("yes")