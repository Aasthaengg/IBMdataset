import sys
s = input()
for one in range(97,97+26):
    c = chr(one)
    if not c in s:
        print(c)
        sys.exit()
print("None")