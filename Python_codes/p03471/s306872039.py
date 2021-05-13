N, Y = map(int, input().split())

ans = [-1, -1, -1]
for x in range(N+1):
    a = 10000*x
    for y in range(0, (N+1)-x):
        b = 5000*y
        z = N-(x+y)
        c = 1000*z
        if (a+b+c) == Y:
            ans = [x, y, z]
            break
ans = map(str, ans)
print(" ".join(ans))