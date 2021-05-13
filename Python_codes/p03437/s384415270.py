X, Y = list(map(int, input().split()))

if X % Y == 0:
    ans = -1
else:
    for i in range(1, 10**18):
        t = X * i
        if t % Y != 0:
            ans = t
            break

print(ans)