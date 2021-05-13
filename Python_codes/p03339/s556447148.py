#!/usr/bin/env python3
n = int(input())
s = input()

lww = 0
lee = s[1:].count("E")
ans = lww + lee

for i in range(1, n):
    if s[i] == "E":
        lee -= 1
    if s[i - 1] == "W":
        lww += 1

    ans = min(ans, lee + lww)
    
print(ans)