import math
L, R = map(int, input().split())

if (R - L) >= 2019:
    print(0)
else:
    ans = math.inf
    for i in range(L, R):
        for j in range(i+1, R+1):
            ans = min(ans, ((i%2019)*(j%2019))%2019)
    print(ans)