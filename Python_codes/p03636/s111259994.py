import sys
s = input()
if len(s) < 3 or len(s) > 100:
    sys.exit()

print(s[0:1]+str((len(s)-2))+s[-1])