X, Y = map(int, input().split())
ans = (Y - 1) * X
if ans % Y == 0:
    print(-1)
else:
    print(ans)
