#!/usr/bin/env python3
n, *h = map(int, open(0).read().split())
ans = 0
b = ["1"] * n
while sum(h) > 0:
    for i in range(n):
        if h[i] > 0:
            h[i] -= 1
        else:
            b[i] = "0"
    ans += sum(i != "" for i in "".join(b).split("0"))
print(ans)
