#/usr/bin/env python

n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0 
v = 0 
for i in range(n):
    v = a[v]-1
    ans += 1
    if v == 1:
        print(ans)
        exit()

print(-1)
