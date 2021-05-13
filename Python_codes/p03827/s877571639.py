import os
import sys
import math
if os.environ.get("DEBUG") is not None:
    sys.stdin = open("in.txt", "r")
rl = sys.stdin.readline

n, s = rl().rstrip("\n"), rl().rstrip("\n")
x = 0
ans = 0
for it in s:
    if it == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)