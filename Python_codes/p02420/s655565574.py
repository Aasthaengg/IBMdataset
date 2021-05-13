# coding: utf-8
# Your code here!

while True:
    n = str(input())
    if n == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        n = n[h:] + n[:h]
    print(n)
