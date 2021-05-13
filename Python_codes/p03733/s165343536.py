N, Y = map(int, input().split())
T = list(map(int, input().split()))

last = -1
ans = 0
for t in T:
    if t <= last:
        ans += Y - (last - t)
    else:
        ans += Y
    last = t + Y

print(ans)
