import sys

s = input()

for c in s[::2]:
    if(c == 'L'):
        print("No")
        sys.exit()

for c in s[1::2]:
    if(c == 'R'):
        print("No")
        sys.exit()

print("Yes")