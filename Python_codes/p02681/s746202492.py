import sys
s = input()
t = input()

for i in range(len(s)):
    if s[i] != t[i]:
        print("No")
        sys.exit()
else:
    print("Yes")
