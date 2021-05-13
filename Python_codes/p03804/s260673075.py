#!/usr/bin/env python

n, m = map(int, input().split())
a = [['' for _ in range(n)] for _ in range(n)]
b = [['' for _ in range(m)] for _ in range(m)]
for i in range(n):
    a[i] = input()
for i in range(m):
    b[i] = input()

for i in range(n-m+1):
    ok = True
    for j in range(n-m+1):
        ok = True
        for p in range(m):
            for q in range(m):
                if b[p][q] != a[i+p][j+q]:
                    ok = False
                    break
        if ok: 
            print('Yes')
            exit()

print('No')
