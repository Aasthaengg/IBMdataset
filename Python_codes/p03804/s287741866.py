#!/usr/bin/env python3
n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if all(b[k] == a[i + k][j:j + m] for k in range(m)):
            print("Yes")
            exit()
print("No")
