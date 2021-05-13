import sys
s = input()
if not s.islower():
    sys.exit()
if len(s) < 0 or len(s) > 10 ** 5:
    sys.exit()

print(s[::2])