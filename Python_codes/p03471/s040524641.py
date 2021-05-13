n, y = map(int, input().split())

for a in range(n+1):
    for b in range(n+1):
        c = max(n - (a + b), 0)
        if a+b+c == n and 10000*a + 5000*b + 1000*c == y:
            print(a, b, c)
            exit()
print(-1, -1, -1)