N = int(input())
import math
ans = 0
for k in range(1, int(math.sqrt(N) + 1)):
    # print(k - 1, N // k - 1)
    m = N // k - 1
    if m != 0:
        if N % k == 0 and N // m == N % m:
            ans += m

print(ans)
