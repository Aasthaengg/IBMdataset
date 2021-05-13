# coding: utf-8

(r, d, x2000) = map(int, input().rstrip().split(" "))

current = x2000
for i in range(1, 11):
    current = r * current - d
    print(current)
