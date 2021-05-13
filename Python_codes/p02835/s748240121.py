A = list(map(int, input().split()))

ans = "bust"


if sum(A[:3]) <= 21:
    ans = "win"


print(ans)