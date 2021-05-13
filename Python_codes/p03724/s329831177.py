n, m = map(int, input().split())

dis = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    dis[a] += 1
    dis[b] += 1

for i in range(n):
    if dis[i] % 2 == 1:
        print("NO")
        exit(0)

print("YES")
