import numpy as np
n, m = map(int, input().split())

k = [[] for i in range(4)]

for i in range(m):
    s, c = map(int, input().split())
    if s == 1:
        k[1].append(c)
    elif s == 2:
        k[2].append(c)
    else:
        k[3].append(c)

ans = 0
for x in range(1, n+1):
    if len(k[x]) == 0:
        if x == 1 and x != n:
            ans += 10**(n-x)
    elif len(k[x]) == 1 or np.std(k[x]) == 0:
        if k[x][0] == 0 and x == 1 and x != n:
            print(-1)
            exit()
        else:
            ans += (10**(n-x))*k[x][0]
    else:
        print(-1)
        exit()

print(ans)