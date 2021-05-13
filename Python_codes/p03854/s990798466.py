# coding: utf-8
import math
s = input()

while len(s) > 0:
    if s.endswith("dream"):
        s = s[:len(s) - 5]
    elif s.endswith("dreamer"):
        s = s[:len(s) - 7]
    elif s.endswith("erase"):
        s = s[:len(s) - 5]
    elif s.endswith("eraser"):
        s = s[:len(s) - 6]
    else:
        print("NO")
        exit()
print("YES")