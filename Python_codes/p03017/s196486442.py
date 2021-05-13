#!/usr/bin/env python3
n, a, b, c, d = map(int, input().split())
s = input()
if c < d:
    print("YNeos"[any(s[i:i + 2] == "##" for i in range(a, d - 1))::2])
else:
    if any(s[i:i + 3] == "..." for i in range(b - 2, d - 1)):
        if all(s[i:+2] != "##" for i in range(a, c - 1)):
            print("Yes")
            exit()
    print("No")
