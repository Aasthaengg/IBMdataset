import sys
s=sys.stdin.readlines()
print(len(set(s[1].split())&set(s[3].split())))
