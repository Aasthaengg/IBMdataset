L, R = [int(_) for _ in input().split()]

diff = R - L
if diff >= 2019:
    print("0")
else:
    ans = min([i * j % 2019 for j in range(L + 1, R + 1) for i in range(L, R)])
    print(ans)
