n, y = map(int, input().split())
y = y // 1000
for a in range(n+1):
    b = (y - n - 9 * a) // 4
    c = n - a - b
    if 0 <= b and 0 <= c and a * 10 + b * 5 + c == y:
        print(a,b,c)
        exit(0)
print(-1,-1,-1)