import sys
readline = sys.stdin.readline
SET = set()
input()
for s in sys.stdin:
    if s[0] == "i":
        SET.add(s[7:])
    elif s[0] == "f":
        print("yes" if s[5:] in SET else "no")

