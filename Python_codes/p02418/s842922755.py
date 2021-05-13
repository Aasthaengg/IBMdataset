import sys
s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
if (s + s).find(p) == -1:
    print("No")
else:
    print("Yes")