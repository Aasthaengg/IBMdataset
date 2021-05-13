#!/usr/bin/env python3
n = int(input())
x_y = [list(input().split()) for _ in range(n)]
ans = 0
for i in range(n):
    if x_y[i][1] == "JPY":
        ans+=float(x_y[i][0])
    else:
        ans+=float(x_y[i][0])*380000
print(ans)
