#coding: utf-8

r, c = (int(i) for i in input().split())

s = [[0 for i in range(c+1)] for j in range(r+1)]

for i in range(r):
    s[i] = input().split()
    s[i].append(0)

for i in range(r):
    for j in range(c):
        s[i][j] = int(s[i][j])

for i in range(r):
    x = 0
    for j in range(c):
        x += s[i][j]
    s[i][-1] = x

for i in range(c+1):
    x = 0
    for j in range(r):
        x += s[j][i]
    s[-1][i] = x

for i in range(r+1):
    for j in range(c+1):
        print(s[i][j], end = ' ' if j != c else '\n')
