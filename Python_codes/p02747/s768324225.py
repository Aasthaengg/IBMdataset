import sys

s = list(map(str,input()))

if len(s)%2 == 1:
    print("No")
    sys.exit()

for i in range(len(s)):
    if i%2 == 0:
        if s[i] != "h":
            print("No")
            sys.exit()
    else:
        if s[i] != "i":
            print("No")
            sys.exit()

print("Yes")