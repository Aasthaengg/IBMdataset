import sys
s = sys.stdin.readline().rstrip()
print(s[0]+str(len(s[1:-1]))+s[-1])