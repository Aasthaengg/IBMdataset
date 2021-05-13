a, b, c, k = map(int, input().split())

if k % 2:
    print(-1 * (a-b))
else:
    print(a-b)