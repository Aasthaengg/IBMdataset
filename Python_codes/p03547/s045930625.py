import sys
s = list(input().split())
if s[0] == s[1]:
    print("=")
    sys.exit()
r = sorted(s)
if s == r:
    print("<")
else:
    print(">")