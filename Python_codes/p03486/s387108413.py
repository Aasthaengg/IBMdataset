#!/usr/bin/env python3

s = sorted(input())
t = sorted(input(), reverse=True)

ans = ""
for x,y in zip(s,t):
    if x > y:
        ans = "No"
        break
    elif y > x:
        ans = "Yes"
        break

if ans == "":
    if len(s) < len(t):
        ans = "Yes"
    else:
        ans = "No"

print(ans)

