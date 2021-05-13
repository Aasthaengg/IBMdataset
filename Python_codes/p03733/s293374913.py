n, T = map(int, input().split())
*t, = map(int, input().split())

ans = 0
for i in range(n-1):
    diff = t[i+1] - t[i]
    ans += diff if diff <= T else T

else:
    ans += T
print(ans)
