#!/usr/bin/env python3
s = input()
Q = int(input())
q = [input().split() for _ in range(Q)]
reverse = 0
start = ""
end = ""
for i in q:
    if i[0] == "1":
        reverse ^= 1
    else:
        if (int(i[1]) + reverse) % 2:
            start += i[2]
        else:
            end += i[2]
s = start[::-1] + s + end
print(s[::1 - reverse * 2])
