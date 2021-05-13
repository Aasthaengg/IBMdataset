import sys

s = input()
for i in range(len(s)):
    if ((i+1) % 2 == 1):
        if (s[i] == 'L'):
            print("No")
            sys.exit()
    elif ((i+1) % 2 == 0):
        if (s[i] == 'R'):
            print("No")
            sys.exit()
print("Yes")