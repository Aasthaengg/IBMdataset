import math
t = 1
for tc in range(t):
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        j = 1
        ans += (n-1) // i
        # while i*j + 1 <= n:
        #     ans += 1
        #     j += 1
    print(ans)
