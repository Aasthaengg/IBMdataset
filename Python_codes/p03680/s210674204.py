#/usr/bin/env python

n = int(input())
a = [int(input()) for _ in range(n)]

lighted = [0] 
ans = 0 

for i in range(n):
    u = lighted[-1]
    v = a[u]-1
    ans += 1
    if v == 1:
        print(ans)
        exit()
    lighted.append(v)

print(-1)
