n, k = map(int, input().split())

if (n-1)*(n-2)//2 < k:
    print(-1)
    exit()

E = []
for i in range(n-1):
    E.append((1, i+2))

for i in range(2, n):
    for j in range(i+1, n+1):
        E.append((i, j))

m = n-1 + (n-1)*(n-2)//2 - k
print(m)
for i in range(m):
    print(*E[i])
