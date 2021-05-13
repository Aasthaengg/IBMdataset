import sys

n = int(input())
a = [int(x) for x in input().split()[::-1]]

if 0 < n and a[-1] != 0:
    print(-1)
    sys.exit()

if n == 0:
    if a[0] == 1:
        print(1)
    else:
        print(-1)
    
    sys.exit()

limit = [[a[0], a[0]]]
for i in range(0, n):
    low = -(-limit[i][0] // 2) + a[i + 1]
    high = limit[i][1] + a[i + 1]
    
    limit.append([low, high])
    
limit = limit[::-1]
a = a[::-1]

if 1 < limit[0][0]:
    print(-1)
    sys.exit()

ans, leaf = 1, 2
for i in range(1, n):
    ans += min(limit[i][1], leaf)
    leaf = 2 * (leaf - a[i])
    
ans += a[n]
print(ans)